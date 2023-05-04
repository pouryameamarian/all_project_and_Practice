def is_symmetrical(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10 ### ---> temp = temp//10 ##### // = / + gerd kardan be payin 13//3 = 4 
    return total == num
num = int(input('Enter any number: '))
if is_symmetrical(num):
    print('The given number is SYMMETRICAL!!')
else:
    print('The given number is NOT SYMMETRICAL!!!')