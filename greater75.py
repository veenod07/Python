def push(s,i):
    s.append(i)  #pushing into stack
def pop(s):
    if s!=[]: #checking if stacks not empty and popping if not empty
        return s.pop()
    else: #if empty reuturn none
        return None

student={"a":78 , "b": 89,"c":56,"d":90,"e":67,"f":98}
s = [] #stack ready
for i in student:
    if student[i] > 75:  #checking for marks greater than 75
        push(s,i)  #calling function push

while True:
    if s!=[]:
        print(pop(s))  #calling pop function
    else:
        break


'''
Ali has a list containing 10 integers.
you need to create a program with seperate user
defined functions to perform the following operations
based on the list.

1)  Traverse the content of the list and push the 
    even numbers into a stack.

2)  pop and display the content of the stack.

'''