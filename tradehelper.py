from thstatuses import STATUS, getTextFromStatus
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from pynput.keyboard import Key, Controller

from multiprocessing.pool import ThreadPool
from thgui import Ui_MainWindow
import pygetwindow as gw
import sys, time
import requests
import pyperclip


# Define a trade class which represents one individual trade
class Trade:
    def __init__(self, wtid, webelement, price, money, text, contactButton, usrname):
        self.tradeid = wtid
        self.webelement = webelement
        self.price = price
        self.money = money
        self.contactButton = contactButton
        self.username = usrname
        self.tradeText = text

    def getID(self):
        return self.tradeid

    def getPrice(self):
        return self.price

    def getMoney(self):
        return self.money

    def getUser(self):
        return self.username

    def contactUser(self):
        # Get all windows with 'Path of Exile' in title
        activewindows = gw.getWindowsWithTitle('Path of Exile')

        # Adding trade to all trades
        allTradesList.append(self.getID())

        gameOpen = False
        for w in activewindows:
            if w.title == "Path of Exile":
                w.activate()
                gameOpen = True
                time.sleep(0.2)
                break

        # If there is an instance of PoE opened
        if gameOpen:
            # Copy text to clipboard
            pyperclip.copy(self.tradeText)

            # Press keys
            keyboard.press(Key.enter)
            time.sleep(0.05)
            keyboard.release(Key.enter)
            keyboard.press(Key.ctrl)
            time.sleep(0.05)
            keyboard.press('a')
            time.sleep(0.05)
            keyboard.release(Key.ctrl)
            keyboard.release('a')
            time.sleep(0.05)
            keyboard.press(Key.ctrl)
            time.sleep(0.05)
            keyboard.press('v')
            time.sleep(0.05)
            keyboard.release(Key.ctrl)
            keyboard.release('v')
            keyboard.press(Key.enter)
            time.sleep(0.05)
            keyboard.release(Key.enter)
        else:
            window.gameOpenedPopUp()


def tradeClicked():
    print("Trade Clicked!")
    global tradeList
    tradeList[window.name_list.currentRow()].contactUser()


# Setup main window and links all functions
def setupWindow():
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.name_list.itemClicked.connect(tradeClicked)
    ui.start_button.clicked.connect(startButtonClicked)
    ui.stop_button.clicked.connect(stopButtonClicked)
    ui.resume_button.clicked.connect(resumeButtonClicked)
    ui.start_button.setEnabled(False)
    ui.show()
    return ui


def searchTrades(drv, minp, maxp, available):
    # Get trade icons (this will make sure that the page is loaded fully)
    try:
        pricePicPath = "/html/body/div[1]/div/div[1]/div[5]/div[6]/div[2]/div[1]/div[2]/div/span[3]/div/img"
        WebDriverWait(drv, 10).until(EC.presence_of_element_located((By.XPATH, pricePicPath)))
    except TimeoutException:
        changeStatus(STATUS.ERROR_LOADING)
        return -1

    # Get refresh button
    refreshButton = drv.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[5]/div[4]/div[2]/div[2]/button")

    # Minimize window and get paths for icons
    # drv.minimize_window()
    allTrades = drv.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[5]/div[6]/div[2]")
    pricePic = allTrades.find_element_by_xpath(".//div[1]/div[2]/div/span[3]/div/img")
    moneyPic = allTrades.find_element_by_xpath(".//div[1]/div[2]/div/span[1]/div/img")

    # Download and save icons
    r = requests.get(pricePic.get_attribute('src'), stream=True)
    open('priceicon.png', 'wb').write(r.content)

    r = requests.get(moneyPic.get_attribute('src'), stream=True)
    open('payicon.png', 'wb').write(r.content)

    # Display icons
    window.price_img.setPixmap(QPixmap('priceicon.png').scaledToHeight(32))
    window.money_img.setPixmap(QPixmap('payicon.png').scaledToHeight(32))

    # Trades that will be displayed next iteration
    availableTrades = []
    global tradeList

    # Clearing window
    window.name_list.clear()
    window.price_list.clear()
    window.money_list.clear()

    # Hard code wait function
    time.sleep(0.5)
    app.processEvents()
    time.sleep(0.5)

    # Initialise webtrade container xpath
    webtradesxpath = "/html/body/div[1]/div/div[1]/div[5]/div[6]/div[2]/div[@class='row exchange']"
    webtrades = drv.find_elements_by_xpath("/html/body/div[1]/div/div[1]/div[5]/div[6]/div[2]/div[@class='row exchange']")

    changeStatus(STATUS.RUNNING)
    while appStatus == STATUS.RUNNING:
        # Start timer
        startTime = time.time()
        print(" === Starting new Iteration ===")
        availableTrades.clear()
        print("Cleared availableTrades")
        # Get Trade Container
        try:
            WebDriverWait(drv, 10).until(EC.presence_of_element_located((By.XPATH, webtradesxpath)))
            webtrades = drv.find_elements_by_xpath("/html/body/div[1]/div/div[1]/div[5]/div[6]/div[2]/div[@class='row exchange']")
        except TimeoutException:
            print("How slow is your internet god damn")

        numberOfFoundTrades = 0
        for webtrade in webtrades:
            if numberOfFoundTrades < 10:
                price = float(webtrade.find_element_by_xpath(".//div[2]/div/span[3]/div/span[1]").text)
                money = float(webtrade.find_element_by_xpath(".//div[2]/div/span[1]/div/span[3]").text)
                # Create trade object
                if maxp >= (price / money) >= minp and available >= price:
                    contactbtn = webtrade.find_element_by_xpath(".//div[3]/div/div[2]/span/button[1]")
                    name = webtrade.find_element_by_xpath(".//div[3]/div/div[1]/span[2]/span/a").text
                    wtID = webtrade.get_attribute("data-id")
                    contactbtn.click()
                    tradetext = webtrade.find_element_by_xpath(".//div[4]/div/div[2]/textarea").text
                    trade = Trade(wtID, webtrade, price, money, tradetext, contactbtn, name)
                    availableTrades.append(trade)
                    numberOfFoundTrades += 1
            else:
                break
        print("Got trades...")
        # Update status bar
        global numberOfTrades
        numberOfTrades = len(availableTrades)
        print("Updated status bar")
        print("Printing number of trades:", len(availableTrades))

        print("Clearing GUI")
        tradeList.clear()
        window.name_list.clearSelection()
        window.name_list.clear()
        window.price_list.clear()
        window.money_list.clear()

        print("Adding trades to list")
        for t in availableTrades:
            tradeList.append(t)
            window.name_list.addItem(t.getUser())
            window.price_list.addItem(str(t.getPrice()))
            window.money_list.addItem(str(t.getMoney()))

        if window.isAutoTextChecked():
            for t in tradeList:
                if t.getID() not in allTradesList:
                    t.contactUser()
                    app.processEvents()
                    time.sleep(0.1)

        print(" Execution time: ", time.time() - startTime)
        print(" === Ending Iteration === \n\n")

        # More trades sleep less
        time.sleep(reloadTime - len(availableTrades) / 4)
        try:
            WebDriverWait(drv, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div[5]/div[4]/div[2]/div[2]/button")))
        except TimeoutException:
            print("What is this...")
        refreshButton.click()


def openWebDriver():
    # driver wait 2 seconds and driver minimize
    drv = webdriver.Firefox()
    drv.get("https://www.pathofexile.com/trade/exchange/Delirium/")
    if window.closeWindow:
        drv.quit()
    return drv


# Start Button clicked
def startButtonClicked():
    if appStatus == STATUS.NONE or appStatus == STATUS.NOT_ALL_INPUT or appStatus == STATUS.INVALID_INPUT or appStatus == STATUS.RUNNING or appStatus == STATUS.ERROR_LOADING:
        changeStatus(STATUS.STARTING)

        # Get inputs from ui
        baseurl = "https://www.pathofexile.com/trade/exchange/Delirium/"
        tradeurl = window.getTradeCode()
        minimumPrice = window.getMinimumPrice()
        maximumPrice = window.getMaximumPrice()
        availableCurrency = window.getAvailableCurrency()

        # Check if all input fields are filled
        if tradeurl == -1 or minimumPrice == -1 or maximumPrice == -1 or availableCurrency == -1:
            changeStatus(STATUS.NOT_ALL_INPUT)
            print("Not all input!")
        # Check if all input are valid
        elif tradeurl == -2 or minimumPrice == -2 or maximumPrice == -2 or availableCurrency == -2:
            changeStatus(STATUS.INVALID_INPUT)
            print("Invalid input!")
        # If every input is good proceed
        else:
            url = baseurl + tradeurl
            driver = driverThread.get()
            driver.get(url)
            # Start trading thread
            pool.apply_async(searchTrades, (driver, minimumPrice, maximumPrice, availableCurrency,))


# Stop Button clicked
def stopButtonClicked():
    if appStatus == STATUS.RUNNING:
        changeStatus(STATUS.STOPPING)

        timer = 0
        while timer <= reloadTime:
            time.sleep(0.02)
            app.processEvents()
            timer += 0.02

        window.name_list.clear()
        window.price_list.clear()
        window.money_list.clear()
        tradeList.clear()
        changeStatus(STATUS.NONE)


# Resume Button clicked
def resumeButtonClicked():
    print("How did u get here?.. Are you hacking my app?")
    print("Pretty cool tho, what do you think.")


# Function to change the current status
def changeStatus(sts: STATUS):
    global appStatus
    appStatus = sts


# Main Loop for status
def updateStatus():
    while not window.closeWindow:
        statusText = getTextFromStatus(appStatus, numberOfTrades)
        window.status.setText(statusText)
        # Disable Start button until webdriver is loaded
        if appStatus != STATUS.LOADING and not window.start_button.isEnabled():
            window.start_button.setEnabled(True)
        # Change status when webdriver is loaded
        if appStatus == STATUS.LOADING and driverThread.get():
            changeStatus(STATUS.NONE)
        time.sleep(0.1)
    drv = driverThread.get()
    drv.close()
    drv.quit()


if __name__ == "__main__":
    # Thread pool
    pool = ThreadPool(processes=4)

    # Local app and webdriver
    app = QApplication(sys.argv)
    driverThread = pool.apply_async(openWebDriver)

    # Variables
    appStatus = STATUS.LOADING
    window = setupWindow()
    numberOfTrades = 0
    reloadTime = 3
    startedAtLeastOneTrade = False

    # Trades that are currently displayed on the GUI
    tradeList = []
    # List of all current session trades
    allTradesList = []

    # Initialise keyboard
    keyboard = Controller()

    # Status bar thread
    statusThread = pool.apply_async(updateStatus)

    # Terminate the program when window is closed
    sys.exit(app.exec_())
