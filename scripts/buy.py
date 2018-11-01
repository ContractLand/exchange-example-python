from web3 import Web3
import json
from dotenv import load_dotenv
from pathlib import Path  # python3 only
import os

env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)


fo = open("../abis/Exchange.abi.json", "r")
Exchange=json.load(fo)
fo.close()

fo = open("../abis/ERC827.abi.json", "r")
ERC827=json.load(fo)
fo.close()

CLC_ADDRESS = '0x0000000000000000000000000000000000000000'

web3Instance = Web3(Web3.HTTPProvider("https://gaia.terrachain.network" ,request_kwargs={'timeout':240}))

erc827 = web3Instance.eth.contract(abi=ERC827, address=os.getenv('ETH_TOKEN_ADDRESS'))
exchange = web3Instance.eth.contract(abi=Exchange, address=os.getenv('EXCHANGE_ADDRESS'))

tradeTokenAmount = 0.1
tradePrice = 2
baseTokenAmount = tradeTokenAmount * tradePrice

def main():
  

   
    nonce = web3Instance.eth.getTransactionCount(os.getenv('USER_ADDRESS'))
    
    buyData = exchange.functions.buy(os.getenv('ETH_TOKEN_ADDRESS'), CLC_ADDRESS,  os.getenv('USER_ADDRESS'), web3Instance.toWei(str(tradeTokenAmount),'ether'), web3Instance.toWei(str(tradePrice),'ether')).buildTransaction({'gas': 500000, 'gasPrice': web3Instance.toWei('1', 'gwei'),'nonce': nonce,})
    
    
    
    txData = erc827.functions.approveAndCall(os.getenv('EXCHANGE_ADDRESS'), web3Instance.toWei(baseTokenAmount,'ether'), buyData['data']).buildTransaction({'gas': 500000, 'gasPrice': web3Instance.toWei('1', 'gwei'),'nonce': nonce,})
    
    
    
    signed_txn = web3Instance.eth.account.signTransaction(txData, private_key=os.getenv('USER_ADDRESS_PRIVATE_KEY'))
    txhash=web3Instance.eth.sendRawTransaction(signed_txn.rawTransaction)   
    print(txhash.hex())
  
main()