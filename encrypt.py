def encrypt(a,b):
    return b.join(a)

def decrypt(e,b):
    return e.split(b)  #### p$r$e$m.split("$")

def hello():
    print("hello")

a = input("Enter a String: ")
b = input("enter the symbol: ")

e = encrypt(a,b)
print(e)
d = decrypt(e,b)
print(d)
g = ""
f = encrypt(d,g)
print("encrypted text : ",e)
print("decrypted text : ", f)

h = hello()

