import sys
f = open("data.txt")
'''line1 = f.readline()
line2 = f.readline()
sys.stdout.write(line1)
sys.stdout.write(line2)
sys.stderr.write("no error")'''
for line in f:
    print(line)
f.close()
