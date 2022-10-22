# 1
# 2 2
# 3 3 3
# 4 4 4 4

# for i in range(4):
#     for j in range(i+1):
#         print(i+1, end ="")
#     print("")

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# num = int(input("row: "))
# mid = num / 2
# for i in range(num):
#     if i < mid:

# new_quiz_3
input_number = int(input("Please input your number : "))
counter = input_number

for i in range(1, counter + 1):
    if i == counter: # final round
        print("z")
        break

    for row in range(0, counter + 1 - i): # up pyramid
        if i > 1 and row == 0:
            continue
        for colum in range(row + 1):
            print(f"x ", end="")
        print("")
    
    for row in range(counter - i, 0, -1): # down pyramid
        for colum in range(row):
            print(f"y ", end="")
        print("")