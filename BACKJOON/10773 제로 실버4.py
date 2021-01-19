N = int(input())
queue = []
for i in range(N):
    num = int(input())
    if num != 0:
        queue.append(num)
    else:
        queue.pop()
print(sum(queue))
