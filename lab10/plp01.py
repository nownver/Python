
#---------------self--------------------
def plp():
    lst = []
    x = 1
    while True:
        name = input(f"Enter name{x}: ")
        lst.append(name)
        if len(name) == 0:
            lst.pop()
            break
        x += 1
    print(lst)
plp()

#------------------TA-------------------

# def name_list():
#     names = []
#     time = 2
#     name = input("Enter a name 1: ")
#     while name != "":
#         names.append(name)
#         name = input("Enter a name " + str(time) + ": ")
#         time += 1
#     return names

# print(name_list())

#------------jeff-----------------------

# def name_list():
#     x = 0
#     lst = []
#     while True:
#         x += 1
#         name = input(f'Enter name {x}: ')
#         if name != '':
#             lst.append(name)
#         else:
#             print(lst)
#             break
        
# name_list()
        

#------------pTawan----------
# 63011335 Tawan Lekngam
# Lab10 Q1

# def name_list() -> list:
#     index = 0
#     name = input(f"Enter name {index + 1}: ").strip()
#     res = list()
#     while len(name) != 0:
#         res.append(name.capitalize())
#         index = index + 1
#         name = input(f"Enter name {index + 1}: ")
#     return res


# if __name__ == "__main__":
#     print(name_list())
