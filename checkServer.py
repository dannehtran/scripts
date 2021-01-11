# This script will verify if the host has a valid SSL certificate using the requests library and specifying a directory of local CAs
# It will then have a conditional statement that either allows the host to curl the server or deny it

# Imports the requests and JSON libraries
import requests
import json

# Function that checks the SSL of the host using a local directory CA store
def checkSSL(hostname, dirPath):
	getRes = requests.get(hostname, verify=dirPath)
	if getRes.status_code == 200:
		sslResults = str(getRes)
		return "[SSL Verification] Client received an OK " + sslResults
	else:
		return "[SSL Verification] Client could not verify SSL"

# Function that checks the header response of the host
def checkHead(hostname):
	headRes = requests.head(hostname)
	if headRes.status_code == 200:
		headResults = str(headRes)
		return "[Header] Client received an OK " + headResults
	else:
		return "[Header] Client received an " + headResults

# Function that checks the POST response of the host
def checkPost(hostname):
	postRes = requests.post(hostname)
	if postRes.status_code == 200:
		postResults = str(postRes)
		return "[POST] Client received an OK " + postResults
	else:
		return "[POST] Client received an " + postResults

# Main function that loads the config.json file to attach enviromental variables to code
def __init__():
	with open('configs/ssl_configs.json', 'r') as cfg_file:
		config = json.load(cfg_file)

		# Assigns hostname and dirPath to the values in the config
		hostname = config['hostname']
		dirPath = config['dirPath']

	# Prints the return call of checkSSL, checkHead, and checkPost functions
	print(checkSSL(hostname, dirPath))
	print(checkHead(hostname))
	print(checkPost(hostname))

# Calling main function
__init__()

