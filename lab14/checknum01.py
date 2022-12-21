# flag = len(lst)
# def member(n, lst):
#     flag -= 1
#     if n == lst[len(lst)-1]:
#         return True
#     # else:
#     # if n != lst[1] or n != lst[0]:
#     #     return False
#     if flag == len(lst):
#         if 
#     member(n, lst[1:len(lst)-1])
    
#     # return False

# print(member(1,[1,3,4,5,2]))

# def nPrintln(message, n):
#     if n >= 1:
#         print(message)
#         nPrintln(message, n - 1)

# nPrintln("yok", 5)

def member(n, lst):
    if lst == []:
        return False
    if n == lst[0]:
        return True  
    return member(n, lst[1:])

print(member(1,[1,3,4,5,2]))