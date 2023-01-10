from sys import maxsize

def maxsub(b,a):
    m = -maxsize - 1
    M = 0

    for i in range(a):
        M = M + b[i]
        if m < M:
            m = M
        if M < 0:
            M = 0
    return m

a = int(input())
b =  list(map(int, input(). split()))
if len(b) == a:
    print(maxsub(b,a))