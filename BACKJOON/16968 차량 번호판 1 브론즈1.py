import sys


A = str(input())

temp = 0

cnt = 1

for i in A:
    if i == 'c':
        if temp == 'c':
            cnt *= 25
        else:
            cnt *= 26
        temp = 'c'
    else:
        if temp == 'd':
            cnt *= 9    
        else:
            cnt *= 10
        temp = 'd'
        
print(cnt)
