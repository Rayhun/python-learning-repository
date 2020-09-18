class Father():

	name = 'Sirajul Haque'
	money = 1

	def smoking():
		print('Father smoking')


class Son(Father):
	pass 

son_obj = Son()
print(son_obj.name)