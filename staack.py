from errno import EMEDIUMTYPE


def push(item):
    s.append(item)

def delete(s):
    if s == []:
        return "invalid index"
    return s.pop(a)


s = [] #empty list
n = int(input("enter no of items: "))
for i in range(n):
    item = input("enter the element: ")
    push(item)

print(s)

print(delete(s))





