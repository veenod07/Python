student = {}
n = int(input("enter no of students: "))
for i in range(n):
    key = input("enter student name: ")
    value = int(input("enter student marks: "))
    student[key] = value

print(student)

def add(s,a):
    return s.append(a)

def delete(s):
    if s!=[]:
        return s.pop()
    else:
        return None

s = []
for i in student:
    if student[i] > 75:
        add(s,i)


while True:
    if s!=[]:
        print(delete(s))
    else:
        break

