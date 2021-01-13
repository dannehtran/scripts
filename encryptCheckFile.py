from cryptography.fernet import Fernet
import os.path
from os import path
import hashlib

class SecureFile:
	keyFile = ''
	filename = ''
	key = ''
	encrypted_file = ''
	encrypted_data = ''
	unencrypted_file = ''
	encondedKey = ''

	def __init__(self):
		return
	# Function that creates a private key in the keys directory.
	def _createKey(self, keyFile):

		# Assign method attribute to keyFile parameter
		self.keyFile = keyFile

		# Check to see if the user is using a pre-existing private key in the path
		checkKey = path.exists(self.keyFile)

		# If true, open up the file and bind the contents of the key to the variable key
		if checkKey == True:

			with open(keyFile, 'rb') as mykey:
				key = mykey.read()
			return key

		# If false, create a private key for the user in keyFile path
		else:

			# Call the generate_key() method and set it to a variable
			generateKey = Fernet.generate_key()

			# Open/create a file called private.key in the current working directory and write the contents of the key variable to it
			with open(keyFile, 'wb') as mykey:
				writeKey = mykey.write(generateKey)

			# Opens the new file in keyFile and reads the contents of the file and assigns it to the readKey variable
			with open(keyFile, 'rb') as newkey:
				key = newkey.read()
			return key

	def encryptFile(self, filename, key):
		self.filename = filename
		self.key = key

		encondedKey = Fernet(self.key)
		
		with open(filename, 'rb') as file:
			unencrypted_data = file.read()
		encrypted_data = encondedKey.encrypt(unencrypted_data)
		encrypted_file = "encrypted_" + self.filename 
		
		with open(encrypted_file, 'wb') as eFile:
			eFile.write(encrypted_data)

		self.encrypted_file = encrypted_file
		self.encrypted_data = encrypted_data
		self.encondedKey = encondedKey

		return filename

	def decryptFile(self):
		self.unencrypted_file = 'decrypt_' + self.filename

		decrypted_data =  self.encondedKey.decrypt(self.encrypted_data)
		with open(self.unencrypted_file, "wb") as file:
			file.write(decrypted_data)
		return self.unencrypted_file


	def checkHash(self, filename):

		with open(filename, "rb") as file:
			chunk = file.read()
			hashedData = hashlib.sha256(chunk).hexdigest()
		return(hashedData)

obj = SecureFile()
keyObj = obj._createKey('test.txt')
encryptObj = obj.encryptFile('someFile.txt', keyObj)
hashCheckObj = obj.checkHash(encryptObj)
decryptObj = obj.decryptFile()
hashCheckDecryptObj = obj.checkHash(decryptObj)

if hashCheckObj == hashCheckDecryptObj:
	print('Both files have matching hashes, secure file')
else:
	print('The decrypted file has been tampered with, deleting file')

