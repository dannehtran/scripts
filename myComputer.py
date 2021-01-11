# Computer class that creates the object
class MyComputer:
	
	# Initialized functions with madatory parameters of name and user
	def __init__(self, name, user):
		self.name = name
		self.user = user

	# Sets the computer's GPU function with one madatory parameter
	def setComputerGPU(self, gpu):
		self.gpu = gpu

# Create an object called X with a name called Danny's Computer and the user as Danny
x = MyComputer("Danny's Computer", "Danny")

# Calls the function within the class in the object X and sets the GPU as RTX 2070 TI
x.setComputerGPU("RTX 2070 TI")

# Creates a dictionary that holds the attributes of the computer
computerDict = {
	'name' : x.name,
	'user' : x.user,
	'gpu' : x.gpu
}

# Print the attributes of the computer object in a json format
print(computerDict)
