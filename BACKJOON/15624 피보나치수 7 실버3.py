import sys
N = int(input())


f2 = 0
f1 = 1
f = 0        

if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    i = 2
    while(i <= N):
        f =  (f1 + f2)%1000000007
        f1,f2 = f,f1
        i += 1
    print(f)
