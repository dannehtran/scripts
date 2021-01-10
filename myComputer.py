class MyComputer:
	computer = "Computer Name"
	gpu = "RTX 3060 TI"
	cpu = "Intel 9700k"

	def computerSpecs(self, computer, gpu, cpu):
		self.gpu = gpu
		self.cpu = cpu
		return "These are your computer specs: " + computer + gpu + cpu
	x = MyComputer()