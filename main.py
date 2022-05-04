from style import style
from halo import Halo
from time import sleep
from datetime import datetime
import logging

def timestamp():
    nowTime = int(datetime.timestamp(datetime.now()))
    timeUnit = datetime.fromtimestamp(nowTime).strftime('%Y-%m-%d %H:%M:%S')
    fomat_dt = f'[{timeUnit}]'
    return fomat_dt

"""""""""""""""""""""""""""
//ERROR LOGGING
"""""""""""""""""""""""""""

log_format = '%(levelname)s: %(asctime)s %(message)s'
logging.basicConfig(filename='./logs/errors.log',
                    level=logging.INFO,
                    format=log_format)

logging.info("*************************************************************************************")
logging.info("For Help & To Learn More About how the bot works please visit our wiki here:")
logging.info("Telegram @lotusntp")
logging.info("*************************************************************************************")

ascii = """

██╗      ██████╗ ████████╗██╗   ██╗███████╗
██║     ██╔═══██╗╚══██╔══╝██║   ██║██╔════╝
██║     ██║   ██║   ██║   ██║   ██║███████╗
██║     ██║   ██║   ██║   ██║   ██║╚════██║
███████╗╚██████╔╝   ██║   ╚██████╔╝███████║
╚══════╝ ╚═════╝    ╚═╝    ╚═════╝ ╚══════╝
                                           


"""
spinneroptions = {'interval': 250,'frames': ['🚀 ', '🌙 ', '🚀 ', '🌕 ', '💸 ']}
print(style().YELLOW + ascii+ style().RESET)

spinner = Halo(text=f'await Buy', spinner=spinneroptions)


print(style.RED +"Set your Address in the keys.json file!" + style.RESET)
