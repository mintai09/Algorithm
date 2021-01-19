import sys

N = int(sys.stdin.readline())

stack = []

for i in range(N):
    
    com = sys.stdin.readline().split()
    
    if com[0] == 'push':
        stack.append(int(com[1]))
    elif com[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    elif com[0] == 'size':
        if not stack:
            print(0)
        else:
            print(len(stack))
    elif com[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif com[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
