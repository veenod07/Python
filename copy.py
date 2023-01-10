f = open("data.txt","r")
e = open("contact.txt","w")
while True:
    a = f.readline()
    if len(a) == 0:
        break  #terminate
    if a[0] == "@":
        continue #continue to the next iteration
    e.write(a)
f.close()
e.close()