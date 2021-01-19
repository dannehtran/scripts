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

	# Function that encrypts a file that takes in two parameters
	def encryptFile(self, filename, key):
		self.filename = filename
		self.key = key

		# Calls the Fernet library to encode the key into bytes
		encondedKey = Fernet(self.key)
		
		# Opens the file we want to encrypt and reads the contents and stores it in a varibale called unencrypted_data
		with open(filename, 'rb') as file:
			unencrypted_data = file.read()

		# Encrypts the data and stores it in the encrypted_data variable
		encrypted_data = encondedKey.encrypt(unencrypted_data)
		encrypted_file = "encrypted_" + self.filename 
		
		# Opens/Creates a new file with the "encrypted" + filename and writes the encrypted_data to the new file
		with open(encrypted_file, 'wb') as eFile:
			eFile.write(encrypted_data)

		self.encrypted_file = encrypted_file
		self.encrypted_data = encrypted_data
		self.encondedKey = encondedKey

		# Retusn the original file name that it encrypted
		return filename

	# Function that decrypts the encrypted data using an enconded key
	def decryptFile(self, filename):
		newFileName = 'decrypt_' + filename

		with open(filename, 'rb') as EncryptFile:
			encrypted_data = EncryptFile.read()

		# Decrpyts the data using the encoded key and stores the result in decrypted_data variable
		decrypted_data =  self.encondedKey.decrypt(encrypted_data)

		# Opens the unencrypted_file and writes the unencrypted data to it
		with open(newFileName, "wb") as DecryptFile:
			DecryptFile.write(decrypted_data)

		# Returns the unencrypted_file name
		return filename

	# Function that checks the hash of the file
	def checkHash(self, filename):

		# Open file that you want to check the hash to
		with open(filename, "rb") as file:

			# Reads the file and stores it in the variable chunk
			chunk = file.read()

			# Uses SHA256 algorithm to check the hash of the file and store it in hashedData variable
			hashedData = hashlib.sha256(chunk).hexdigest()

			# Returns the hashed data
		return(hashedData)

obj = SecureFile()												# Creates the class object
keyObj = obj._createKey('test.txt')								# Calls the _createKey function with some private key
encryptObj = obj.encryptFile('someFile.txt', keyObj) 			# Calls the encryptFile function with a file and the keyObj
hashCheckObj = obj.checkHash('encrypted_someFile.txt')						# Checks the hash of the encrypted obj
print(hashCheckObj)
decryptObj = obj.decryptFile('encrypted_someFile.txt')									# Decrypts
hashCheckDecryptObj = obj.checkHash('encrypted_someFile.txt')
print(hashCheckDecryptObj)

if hashCheckObj == hashCheckDecryptObj:
	print('Both files have matching hashes, secure file')
else:
	print('The decrypted file has been tampered with, deleting file')

