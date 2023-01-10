'''
data file : it stores data specific to an 
        application for later use.

        2 types:
        a> text files  stores info  it uses ASCII or unicode
        b> binary files

open and closing of files

    - read
    -write
    -append

open("<filename>",<permission>)  if u dont provide 
                    permission it will set default as read.
        '''
'''fopen = open("class12.txt","r+")
s  = fopen.write("hello im learning python lommmmm")
f = fopen.read()
print(f)
fopen.close()

"different modes aur unke uses"
read()
readline() 
readlines()'''

'''fopen = open("data.txt","w")
fopen.write("mukesh")
f.flush()
fopen.write("prem")
fopen.close()'''


'''write a program to get roll numbers, names and marks 
of the student of a class 
store the details in a file "details.txt"

strip()   
rstrip()
lstrip()

mukesh


import sys
sys.stdout.write()'''

'''f = open("data.txt",'r+')
a = f.read(5)
b = f.read(2)
d = f.read(5)
print(a)
print(b)
print(d)'''

f = open("data.txt","r")
for a in f:
    w = a.split()
    for i in w:
        for l in i:
            if(l.isdigit()):
                print(l)