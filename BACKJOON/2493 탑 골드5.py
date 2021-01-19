import sys
N = int(input())

stack = []
res = []

towers = list(map(int,input().split()))

for i in range(N):
    tower = towers[i]
    while 1:
        if not stack:
            stack.append([tower,i])
            res.append(str(0))
            break
        else:
            x = stack.pop()
            if x[0] > tower:
                stack.append(x)
                stack.append([tower,i])
                res.append(str(x[1]+1))
                break
print(' '.join(res))
