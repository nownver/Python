#=7
# 1 
# 2 1 
# 4 2 1 
# 8 4 2 1 
# 4 2 1 
# 2 1 
# 1 

# =6
# 1 
# 2 1 
# 4 2 1 
# 4 2 1  
# 2 1 
# 1 

rows = int(input())
cols = 1
mid = rows/2
i = 0
for i in range(rows):
    if i < mid:
        for j in range(i,-1,-1):
            print(2**j,end = " ")
    else:
        for j in range(rows - i - 1, -1, -1):
            print(2**j, end = " ")
    print()


# input_num = int(input("Enter num: "))
# if input_num % 2 == 0:
#     rows = int(((input_num+2) // 2))

#     for i in range(rows):
#         for j in range(i):
#             print(f"{2**(i-j-1)} ", end = "")
#         print("")

#     for i in range(rows-1):
#         for j in range(rows-1-i):
#             print(f"{2**(rows-1-i-j-1)} ", end = "")
#         print("")

# else:
#     rows = int(((input_num+3) // 2))

#     for i in range(rows):
#         for j in range(i):
#             print(f"{2**(i-j-1)} ", end = "")
#         print("")

#     for i in range(rows-1):
#         for j in range(rows-1-i-1):
#             print(f"{2**(rows-1-i-j-1)} ", end = "")
#         print("")

#-----------------------------
# for i in range(4):
#     for j in range(i):
#         print(f"{6- ((j+1) * 2)} ", end = "")
#     print("")
# for i in range(3):
#     for j in range(5-i):
#         print(f"{j+1} ", end = "")
#     print("")


# 1 
# 2 1 
# 4 2 1
# 4 3 2 1 
# 5 4 3 2 1


# for i in range(6):
#     for j in range(i):
#         print(f"{2**(j)} ", end = "")
#     print("")

#     for i in range(rows-1):
#         for j in range(rows-1-i):
#             print(f"{2**(rows-1-i-j-1)} ", end = "")
#         print("")
#---------------