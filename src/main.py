
# import some modules
import json
from web3 import Web3, HTTPProvider

# storing blockchain server ip address
blockchain_address="http://127.0.0.1:7545"

# create a new web3 object to access the network

web3=Web3(HTTPProvider(blockchain_address)) # through HTTP
web3.eth.defaultAccount=web3.eth.accounts[0]

# load the artifact
artifact_path="../build/contracts/madhu.json"
contract_address="0xfd8e93415a42E4E81B8feEe5A0a2f8571081AB41"

# identify the ABI (Application Binary Interface)
with open(artifact_path) as file:
	contract_json=json.load(file)
	contract_abi=contract_json['abi']

# connect with contract
contract = web3.eth.contract(address=contract_address,abi=contract_abi)
print('Connected with Contract')

# push the data first
a=int(input('Enter Sensor Value: '))
tx_hash = contract.functions.insertSensorValue(a).transact()
web3.eth.waitForTransactionReceipt(tx_hash)
print('Transaction is Done')


# read the data from blockchain
data=contract.functions.getLastSensorValue().call()
print(data)
