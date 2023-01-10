def push(s,a):
    return s.append(a)  #[21,42]

def delete(s):
    if s == []:
        return "Stack is empty!!" 
    return s.pop()          #[21]

s = list()  #stack
e = True
while(e):
    print("1. To add element to a stack ")
    print("2. To delete element of a stack ")
    print("3. To display top element of a stack ")
    print("4. To display all element of  stack ")
    print("5. To exit ")

    b =int(input("enter your choice: "))
    if b==1:
        print("enter the number of element to be aDDED: ")
        n = int(input())   #2
        for i in range(n):
            a = int(input("enter the element: "))
            push(s,a)
        #print(s)
    if b==2:
        print(delete(s)) #42
    if b ==3:
        print(s[-1])
    if b==4:
        print(s)
    if(b==5):
        print("your session expired now")
        e=False

