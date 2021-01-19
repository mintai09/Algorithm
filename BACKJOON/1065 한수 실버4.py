num = int(input())

if num <= 99:
    print(num)
else:
    hansu = 99
    for n in range(100, num+1) :
        nums = list(map(int, str(n)))  
        if nums[0] - nums[1] == nums[1] - nums[2] :
            hansu+=1
    print(hansu)
