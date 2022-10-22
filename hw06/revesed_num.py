def revesed_num(n):
    sum = 0
    while n != 0: 
        rem = n % 10
        sum = sum * 10 + rem
        n = n // 10
    return sum

result = revesed_num(3456)
print(result)
