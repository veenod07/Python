def push(stack,i):
    stack.append(i)

def func_pop(stack):
    if stack != []:
        return stack.pop()
    return None


s = input("enter the string: ")
#st = s[::-1]
#print("normal string reverse: ",st)


stack = []
for i in s:
    push(stack,i)

while True:
    if stack != []:
        print(func_pop(stack))
    else:
        break

