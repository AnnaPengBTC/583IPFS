import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE
	url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
	headers = {
		'pinata_apikey: 37e6ad229f4345d03996',
		'pinata_secret_apikey: a1d3e4dea02a3d298cc71a05669b098c747f801276df39ba9d355f8464c9cdb5'
		}
	response = requests.request("POST", url, headers=headers, data={"file": json.dumps(data)})
	cid = response.json()["IpfsHash"]
	return cid
	
def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	url = f"https://gateway.pinata.cloud/ipfs/{cid}"
	headers = {
		'pinata_apikey: 37e6ad229f4345d03996',
		'pinata_secret_apikey: a1d3e4dea02a3d298cc71a05669b098c747f801276df39ba9d355f8464c9cdb5'
		}
	response = requests.get(url, headers=headers)
	data = response.json() if content_type == "json" else response.content
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
