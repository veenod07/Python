
'''
u have to take one user input as string. abcd
another input from random integer 1 to 99. 23
encrypt the user input with random integer.a23b23c23d23
and decrypt the encrypted text. abcd
and print all the variables.(user input, random number,
encrypted text, decrypted text)'''




import welcomeall

a = input()
b = "99"
e = welcomeall.encrypt(a,b)
d = welcomeall.decrypt(e,b)
print(e)
print(d)
f = welcomeall.encrypt(d,"")
print(f)



