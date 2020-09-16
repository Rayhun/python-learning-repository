# ''' function '''

# # def rayhan():
# # 	''' Return Hello '''
# # 	print('Hello Rayhan')

# # def hello(name):
# # 	''' Return Hello '''
# # 	my_name = "Hello {}".format(name)
# # 	print(my_name)

# def hello():
# 	''' Return Hello '''
# 	print('Please enter your name')
# 	name = input()
# 	return name

# # hello('Rayhan')

# # rayhan()


# outout = hello()
# print(outout)

# def myAdd(num1, num2):
# 	return num1 + num2

# print(myAdd(5, 7))


# def isOdd(number):
# 	if number % 2 == 1:
# 		print('The number is odd ', number)
# 	else:
# 		print('The number is even ', number)


# isOdd(2)
# isOdd(3)
# isOdd(59)


# def game_good():
#     hidden_number = 9
#     chance = 3
#     praimeery = 0
#     while chance > praimeery:
#         inputted = int(input(" > "))
#         praimeery += 1
#         if inputted == hidden_number:
#             print("Congress!")
#             break
#         else:
#             print("I'm Sorry :(")
# game_good()

# value = [5,2,5,2,2]
# def f_save():
#     for x_count in value:
#         resate = ""
#         for output in range(x_count):
#             print(output)
#             resate += "X"
# f_save()  


# def game():
# 	hidden_number = 7
# 	inputted = int(input("Enter Your Number: "))
# 	if hidden_number == inputted:
# 		print("Correct", hidden_number)
# 		return inputted
# 	elif hidden_number <= inputted:
# 		print("some small try", inputted)
# 	elif hidden_number >= inputted:
# 		print("some large rty")
# 	else:
# 		print("enter any number")


# # game()


# i = 0
# while i <=5:
# 	match = game()
	
# 	if match:
# 		break

# 	i += 1
def numberis():
	global data
	data = "rayhan"

numberis()
print(data)
