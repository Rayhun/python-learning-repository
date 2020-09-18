# class Car:
# 	''' car class '''

# 	# attributes or property 
# 	name = 'BMW'
# 	color = 'Skyblue'


# 	# methods 
# 	def star():
# 		print('Starting the engine')
# 		gf_name = 'jnina'
# 		return gf_name

# # access 
# print(Car.name)
# Car.star()
# print(Car.star())


class Car:
	name = ''
	color = ''

	def start(self): #  Parameter
		print("Starting the engine")

# Creating a Object
my_car = Car()
my_car.name = "toyota"
print(my_car.name)
my_car.start()

