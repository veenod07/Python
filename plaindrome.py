stack=[]
def func_push(stack,b):
    stack.append(b)

def compare(stack,a):
 for c in range(len(a)):
    if a[c]!=stack.pop():
        return False
 return True
a=input()
for i in a:
     func_push(stack,i)
print(compare(stack,a))
