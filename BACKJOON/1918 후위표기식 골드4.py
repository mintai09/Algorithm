import sys

pre = list(map(str,sys.stdin.readline()))

pre.pop()

stack = []
res = ''
for c in pre:

    if c == '(':
        stack.append(c)
    elif c  == '*' or c  =='/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            res += stack.pop()
        stack.append(c)
    elif c  =='+' or c  =='-':  
        while stack and stack[-1] != '(':
            res += stack.pop()
        stack.append(c)
    elif c == ')':
        while stack and stack[-1] != '(':
            res += stack.pop()
        stack.pop()
    else:
        res += c
else:
    while stack:
        res += stack.pop()

print(res)
