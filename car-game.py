def car_game():
    chance = 3
    primary = 0 
    condition = False
    while chance > primary:
        inputted = str(input("Enter Your Command: ").lower())
        primary += 1
        if inputted == "start":
            if condition:
                print("car on the way")
                break
            else:
                condition = True
                print("car start")
        elif inputted == "stop":
            if condition:
                print("car already stopped!")
                break
            else:
                condition = True
                print("car stop")
        elif inputted == "help":
            print('''
                wright the "start" = car start,
                wright the "stop" = car stop
                ''')
        else:
            print("ask me only \"start\" or \"stop\" & \"help\"")
# car_game()

main = [5,1,1,5,1,1,1]
for num in main:
    print(num*"*")