N = int(input())

num = 0

while N != 0:
    stick = 64
    for i in range(7):
        if stick <= N:
            N -= stick
            num += 1
            break
        stick = stick // 2
        
print(num)
