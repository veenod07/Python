param = True
while param:
    print("enter your choice  to find area")
    print(" 1 for circle\n 2 for square\n 3 for triangle\n 0 for exit ")

    a = int(input()) # this will store user choice
    if(a==1):
        r = int(input("enter the radius: "))
        area = 3.14 * r * r
    elif(a==2):
        a = int(input("enter a side's length: "))
        area = a * a
    elif(a==3):
        b = int(input("enter the base: "))
        h = int(input("enter the height: "))
        area = 0.5 * b * h
    elif(a==0):
        area = "you have exited the program"
        param = False
    else :
        area = "invalid input"

    print(area)


