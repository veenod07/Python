import cal

a = int(input("enter number 1 : "))
b = int(input("enter number 2 : "))

d = True
while d:
    print("1 for add, 2 for sub, 3 for div and 4 for mul: ")
    c = int(input("your choice: "))

    if c == 1:
        cal.add(a,b)
    elif c == 2:
        cal.sub(a,b)
    elif c == 3:
        cal.div(a,b)
    elif c == 4:
        cal.mul(a,b)
    else:
        d = False
