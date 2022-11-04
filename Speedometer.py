print("Welcome to the speedometer")
name = str(input("Enter your name here: "))
def speed(x):
    if x <= 70:
        print(name,"You're good to go")
    elif x > 70:
        advance = x-70
        points = advance/5
        print(name,"Your demerit points are:", points)
        if points <= 11:
            print("You still are good to go")
        elif 11 < points > 25:
            print(name,"Your licence is suspended")
        elif points >=25:
            print(name,"you dramatically exceeded the speed limit")
print(speed(100))
print("Thank you for using this calculation")