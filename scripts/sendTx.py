from web3 import Web3
from dotenv import load_dotenv
from pathlib import Path  # python3 only
import os
env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)
print(os.getenv('RPC_URL'))

def sendTx(rpcUrl,privateKey,data,nonce,gasPrice,amount,gasLimit,to,web3):

    
    signed_txn = client.eth.account.signTransaction(dict(
                                    nonce=int(nonce),
                                    gasPrice=web3.toWei(gasPrice,'ether'),
                                    gas=gasLimit,
                                    to=to,
                                    value=web3.toWei(amount,'ether'),
                                    data=data,
                                  ),
                                  '0x'+privateKey,
                            )  
    bal=client.eth.sendRawTransaction(signed_txn.rawTransaction)
    return bal


d=0