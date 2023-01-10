l = []
a = int(input("enter nummber of items to be added: ")) #5
for i in range(a):
    c = input("enter vowels ") #E
    b = c.lower()  # b = e
    if b == 'a' or b == 'i' or b == 'e' or b == 'o' or b =='u' or b == 'A' or b == 'E':
        l.append(c)
print(l)
