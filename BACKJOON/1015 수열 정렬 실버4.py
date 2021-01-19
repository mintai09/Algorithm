import sys

N = int(input())

A = list(map(int,input().split()))

nums = []

for i in range(N):
    nums.append([i,A[i]])

nums.sort(key = lambda x:x[1])

cal  = []

for i in range(N):
    cal.append([nums[i][0],i])
    
cal.sort(key = lambda x:x[0])
P = [str(num[1]) for num in cal]

print(' '.join(P))
