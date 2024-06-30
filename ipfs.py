import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE
	response = requests.post("https://ipfs.infura.io:5001/api/v0/add", files={"file": json.dumps(data)})
	cid = response.json()["Hash"]
	return cid
	
def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	response = requests.get(f"https://ipfs.infura.io:5001/api/v0/cat?arg={QmPAg1mjxcEQPPtqsLoEcauVedaeMH81WXDPvPx3VC5zUz}")
	data = response.json() if content_type == "json" else response.content
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
