def push(stack,i):
    stack.append(i)

def func_pop(stack):
    if stack == []:
        return
    else:
        return stack.pop()

def compare(a,stack):
     for i in range(len(a)):
        if a[i] != func_pop(stack):
            return False
        return True

a = input("enter the string: ")
stack = []
for i in a:
    push(stack,i) #[n,a,m,a,n]
b = compare(a,stack)
if b:
    print("Entered String is a Palindrome")
else :
    print("not a Palindrome")


