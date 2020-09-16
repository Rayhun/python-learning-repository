for i in range(25):
    inp = int(input("Enter Time: "))
    if inp == 0:
        print(" invalide", "\"Try ", i,  "Time\"")
    elif inp <= 3:
        print("Learning Python ", "\"Try ", i,  "Time\"")
    elif inp <= 8:
        print("Sleeping Time", "\"Try ", i,  "Time\"")
    elif inp <= 9:
        print("Brack first Time", "\"Try ", i,  "Time\"")
    elif inp <= 13:
        print("Web Design", "\"Try ", i,  "Time\"")
    elif inp <= 15:
        print("Lunch Time", "\"Try ", i,  "Time\"")
    elif inp <= 19:
        print("Learning Python Time", "\"Try ", i,  "Time\"" )
    elif inp <= 21:
        print("Refashioned ", "\"Try ", i,  "Time\"")
    elif inp <= 23:
        print("Dinner", "\"Try ", i,  "Time\"")
    else:
        print("Out of range", "\"Try ", i,  "Time\"")