# dont forget to check numbers of digit!!!!


def reverse(num):
    sum = 0
    for i in range(4):
        remain = num % 10
        sum = (sum * 10) + remain
        num = num // 10
    return sum

number_input = int(input("Enter a fo ur-digit integer: "))

if len(str(number_input)) == 4:
    reversed_num = reverse(number_input)
    print(f"Reversed number is {reversed_num}")
else:
    print("Enter four-digit integer only")


# def check(num):
#     # new = ''
#     if len(num) == 4:
#         new = num[::-1]
#     else:
#         new = "enter 4 digit only"
#     return new
    
# number_input = int(input("Enter a four-digit integer: "))
# string_number_input = str(number_input)
# answer = check(string_number_input)
# # new = string_number_input[::-1]
# # print(new)
# print(answer)

# r = check("6775")
# print(r)

