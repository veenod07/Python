print("hello")
a = [2,2,2] #decrease by 1 , increase by 1
k = 1
maximum = a[0]
minimum = a[0]
while k > 0:
    for i in a:
        if i > maximum:
            maximum = i
        if minimum > i:
            minimum = i
    maximum = maximum - 1
    print("maximum :",maximum)
    minimum = minimum + 1
    print("minimum :",minimum)
    k=k-1
print(maximum-minimum)
