
def sum_of_digits(num):
    sum = 0
    for i in range(len(str(num))):
        sum += int((str(num))[i])
    return sum

result = sum_of_digits(501)
print(result)

# def sum(num):
#     sum = 0
#     for i in str(num):
#         sum += int(i)
#     return sum

# print((sum(123)))