class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print('restaurant_name: ' + self.restaurant_name + 'cuisine_type: ' + self.cuisine_type)

	def open_restaurant(self):
		print('正在营业中')

	def set_number_served(self, num):
		self.number_served += num