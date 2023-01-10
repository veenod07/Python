contact=int(input("contact information: "))
myfile=open("contact.txt","w+")
for i in range(contact):
 name=input("name: ")
 number=int(input("number: "))
 rec=name+" "+str(number)+'\n'
 myfile.write(rec)
myfile.seek(0)
#df 12345
print(myfile.read(2)) # df
print(myfile.read(5)) # _1234
myfile.close()

