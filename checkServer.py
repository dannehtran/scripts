# This script will verify if the host has a valid SSL certificate using the requests library and specifying a directory of local CAs
# It will then have a conditional statement that either allows the host to curl the server or deny it

# Imports the requests and JSON libraries
import requests
import json

# Function that checks the SSL of the host using a local directory CA store
def checkSSL(hostname, dirPath):
	results = requests.get(hostname, verify=dirPath)
	return results

# Main function that loads the config.json file to attach enviromental variables to code
def __init__():
	with open('configs/ssl_configs.json', 'r') as cfg_file:
		config = json.load(cfg_file)

		# Assigns hostname and dirPath to the values in the config
		hostname = config['hostname']
		dirPath = config['dirPath']

	# Prints the return call of checkSSL function
	print(checkSSL(hostname, dirPath))

# Calling main function
__init__()

