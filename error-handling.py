
father = input("Father age: ")
mother = input("Mother age: ")
try:
	gap = int(father) - int(mother)
	stn = str(gap)
	print("Age Diffarant :  " + stn)

except ValueError:
	print("Enter Only Number")


