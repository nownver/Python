# input_number = int(input("Please input your number : "))
# counter = input_number

# while 1:
#     if input_number == 1:
#         print("*")
#         break
#     for row in range(1, counter + 1):
#         for colum in range(row):
#             print(f"* ", end="")
#         print("")
#     for row in range(counter - 1, 1, -1):
#         for colum in range(row):
#             print(f"* ", end="")
#         print("")

#     if counter == 0:
#         print("*") # final round
#         break
#     counter = counter - 1


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
