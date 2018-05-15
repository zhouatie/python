class Car():
	def __init__(self, name):
		self.name = name

	def printCarName(self):
		print(self.name)

class ElectricCar(Car):
	def __init__(self, name, price):
		super().__init__(name)
		self.price = price

	def printPrice(self):
		print(self.price)