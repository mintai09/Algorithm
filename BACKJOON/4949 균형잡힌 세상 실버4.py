import sys

while 1:
    s = str(input())
    queue = []
    if s == ".":
        break
    
    for c in s:
        if c == '(':
            queue.append('(')
        elif c == '[':
            queue.append('[')
        elif c == ']':
            if queue and queue[-1] == '[':
                queue.pop()
            else:
                print('no')
                break
        elif c == ')':
            if queue and queue[-1] == '(':
                queue.pop()
            else:
                print('no')
                break
    else:       
        if not queue:
            print('yes')
        else:
            print('no')
