from enum import Enum


class STATUS(Enum):
    NONE = 1
    RUNNING = 5
    LOADING = 10
    STARTING = 11
    STOPPING = 12
    RESUMING = 13
    NOT_ALL_INPUT = -1
    INVALID_INPUT = -2
    ERROR_LOADING = -5
    CLOSING_APP = 999


def getTextFromStatus(status: STATUS, numberOfTrades=0):
    if status == STATUS.NONE:
        txt = "Status: Waiting.."
    elif status == STATUS.RUNNING:
        if numberOfTrades > 1:
            txt = "Status: Found " + str(numberOfTrades) + " Trades!"
        elif numberOfTrades == 1:
            txt = "Status: Found 1 Trade!"
        else:
            txt = "Status: Found no Trades!"
    elif status == STATUS.LOADING:
        txt = "Status: Loading.."
    elif status == STATUS.STARTING:
        txt = "Status: Starting.."
    elif status == STATUS.STOPPING:
        txt = "Status: Stopping.."
    elif status == STATUS.RESUMING:
        txt = "Status: Resuming.."
    elif status == STATUS.NOT_ALL_INPUT:
        txt = "Status: Fill all fields!"
    elif status == STATUS.INVALID_INPUT:
        txt = "Status: Invalid Input!"
    elif status == STATUS.ERROR_LOADING:
        txt = "Error loading webdriver."
    else:
        txt = "unknown status"
    return txt
