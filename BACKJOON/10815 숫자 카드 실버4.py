import sys

N = int(input())

cards = list(map(int,sys.stdin.readline().split()))
cards.sort()

M = int(input())

cheacks = list(map(int,sys.stdin.readline().split()))

result = ['0' for _ in range(M)]

for i in range(M):
    l = 0
    r = N-1
    while l <= r :
        m = (l+r) // 2
        if cards[m] == cheacks[i]:
            result[i] = str(1)
            break;
        elif cards[m] > cheacks[i]:
            r = m -1
        else :
            l = m + 1
   
print(' '.join(result))
