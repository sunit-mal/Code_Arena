def checkArmstrong(n):
    order = len(str(n))
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if n == sum:
        return True
    else:
        return False

n1 = int(input())

if checkArmstrong(n1):
    print("Yes")
else:
    print("No")
