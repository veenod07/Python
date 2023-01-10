
def push(a):
    s =[]
    

    for i in range(len(a)):
        if a[i] % 5==0:
            s.append(a[i])

    if s == []:
        print("stack is empty")
    else:
        print(s)

a = [12,34,55,19,0,45,1,5,10,100]
push(a)
