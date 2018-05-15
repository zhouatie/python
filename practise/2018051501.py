# -- coding: utf-8 --
# from car import Car, ElectricCar
# from restaurant import Restaurant
# from collections import OrderedDict

# class Dog():
# 	def __init__(self, name, age):
# 		"""初始化属性name和age"""
# 		self.name = name;
# 		self.age = age;

# 	def sit(self):
# 		"""模拟小狗被命令时蹲下"""
# 		print(self.name.title() + " is now sitting.")

# 	def roll_over(self):
# 		"""模拟小狗被命令时打滚"""
# 		print(self.name.title() + " rolled over!")


# dog = Dog('ZhouTao', '23')
# dog.sit()
# dog.roll_over()
# print(dog.name)
# print(dog.age)

# class Restaurant():
# 	def __init__(self, restaurant_name, cuisine_type):
# 		self.restaurant_name = restaurant_name
# 		self.cuisine_type = cuisine_type
# 		self.number_served = 0

# 	def describe_restaurant(self):
# 		print('restaurant_name: ' + self.restaurant_name + 'cuisine_type: ' + self.cuisine_type)

# 	def open_restaurant(self):
# 		print('正在营业中')

# 	def set_number_served(self, num):
# 		self.number_served += num

# restaurant = Restaurant('餐厅', 'haha')
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)

# restaurant = Restaurant('餐厅', 'atie')
# print(restaurant.number_served)
# restaurant.set_number_served(10)
# print(restaurant.number_served)

# class IceCreamStand(Restaurant):
# 	def __init__(self, restaurant_name, cuisine_type):
# 		super().__init__(restaurant_name, cuisine_type)

# ice = IceCreamStand('餐厅', 'atie')
# ice.describe_restaurant()


# car = Car('nike')
# car.printCarName()

# electricCar = ElectricCar('benz', '100w')
# electricCar.printCarName()
# electricCar.printPrice()

# restaurant = Restaurant('ZHOU', 'ATIE')
# restaurant.describe_restaurant()

# my_friends = OrderedDict()
# my_friends['a'] = 'gouzong'
# my_friends['b'] = 'gouyi'
# my_friends['c'] = 'goupeng'
# for k,v in my_friends.items():
# 	print('key: ' + k + ' ===  value: ' + v)

# 第十章 读取文件
# with open('pi_digits.txt') as file_object:
# 	contents = file_object.read()
# 	print(contents.rstrip())

# with open('pi_digits.txt') as file_object:
# 	for line in file_object:
# 		print(line.rstrip())

# with open('pi_digits.txt') as file_object:
# 	lines = file_object.readlines()

# for line in lines:
# 	print(line.rstrip())

# 写入文件
# with open('programming.txt', 'w') as file_object:
# 	file_object.write('I love python!\n')

# 添加文件
# with open('programming.txt', 'a') as file_object:
# 	file_object.write('me too!')

# message = input('请输入姓名！')

# with open('guest.txt', 'w') as file_object:
# 	file_object.write(message + '\n')

