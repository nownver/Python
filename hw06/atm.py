def atm(num,divide):
    result = num // divide
    remain = num % divide
    return result, remain

money = int(input("Input your amount of money: "))

divide = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
result = []
rem = [money]

for i in range(len(divide)):
    sign = "notes"
    num_of_result, remain = atm(rem[i], divide[i])
    result.append(num_of_result)
    rem.append(remain)

    if result[i] == 0:
        continue
    if divide[i] <= 10:
        sign = "coins"
    print(f"{divide[i]}-Baht {sign}: {result[i]}")
