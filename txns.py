from web3 import Web3
import json, sys
from style import style
from datetime import datetime
from decimal import * 
# More than 8 Decimals are not supportet in the input from the token buy amount! No impact to Token Decimals!
getcontext().prec = 8

def timestamp():
    nowTime = int(datetime.timestamp(datetime.now()))
    timeUnit = datetime.fromtimestamp(nowTime).strftime('%Y-%m-%d %H:%M:%S')
    fomat_dt = f'[{timeUnit}]'
    return fomat_dt

class TXN():
    def __init__(self,token_address):
        self.w3 = self.connect()
        self.address, self.private_key = self.setup_address()
        self.token_address = Web3.toChecksumAddress(token_address)
        self.token_contract = self.setup_token()
        self.MaxGasInBNB, self.gas_price = self.setupGas()
        
        

    def connect(self):
        with open("./Settings.json") as f:
            keys = json.load(f)
        if keys["RPC"][:2].lower() == "ws":
            w3 = Web3(Web3.WebsocketProvider(keys["RPC"]))
        else:
            w3 = Web3(Web3.HTTPProvider(keys["RPC"]))
        return w3

    def setupGas(self):
        with open("./Settings.json") as f:
            keys = json.load(f)
        return keys['MaxTXFeeBNB'], int(keys['GWEI_GAS'] * (10**9))

    def setup_address(self):
        with open("./Settings.json") as f:
            keys = json.load(f)
        if len(keys["metamask_address"]) <= 41:
            print(timestamp()+style.RED +" Set your Address in the keys.json file!" + style.RESET)
            sys.exit()
        if len(keys["metamask_private_key"]) <= 42:
            print(timestamp()+style.RED +" Set your PrivateKey in the keys.json file!"+ style.RESET)
            sys.exit()
        return keys["metamask_address"], keys["metamask_private_key"]

    def setup_token(self):
        with open("./abis/bep20_abi_token.json") as f:
            contract_abi = json.load(f)
        token_contract = self.w3.eth.contract(address=self.token_address, abi=contract_abi)
        return token_contract




from dateutil import parser
yourdate = parser.parse("2022-02-04T17:05:02.748Z")
print(datetime.strptime("2022-02-04T17:05:02.748Z", "%Y-%m-%dT%H:%M:%SZ"))
