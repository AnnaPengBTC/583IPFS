import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE
	url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
	response = requests.request("POST", url, data={"file": json.dumps(data)})
	cid = response.json()["IpfsHash"]
	return cid
	
def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	response = requests.get(f"https://gateway.pinata.cloud/ipfs/{cid}")
	data = response.json() if content_type == "json" else response.content
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
