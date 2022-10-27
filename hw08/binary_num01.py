
num = int(input('Input integer: '))

def IntegerToBinary(num):
    ans = ""
    while num > 0:
        rem = num % 2
        num = num // 2
        ans = str(rem) + ans
    return ans

def BinarytoInteger(num):
    sum = 0
    index = len(num) - 1

    for i in range(len(num)):
        if num[index] == '0':
            add = (2 ** i) * 0
        else:
            add = (2 ** i) * 1
        sum += add
        index -= 1
    return sum

if num == 0:
    print("The number is zero")

elif num < 0:
    print("The number is negative")

else:
    num_binary = IntegerToBinary(num)
    num_integer = BinarytoInteger(num_binary)

    print(f"{num} to Binary is {num_binary}")
    print(f"{num_binary} to Integer is {num_integer}")