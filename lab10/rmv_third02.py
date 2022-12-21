
#---------------------self--------------
# lst1 = [3,6,6,3,7,2,0,1,5,4,5]

# def rmv_the_thirds(l):
#     for i in range(1,len(l)+1):
#         if i == 1:
#             continue
#         if i %3 == 0:
#             l[i-1] = "a"
#         print(i%3,end = "")
#     print(f"{l}")
#     for i in l:
#         if str(i).isdigit() == False:
#             l.remove(i)
#     print(l)

# rmv_the_thirds(lst1)

 
#-------------------TA-----------------------
def remove_the_thirds(lst):
  del lst[3 - 1::3]
  return lst

# print(remove_the_thirds([1,2,3,4,5,6,7,8,9]))

#-------------------pTawan-----------------------
# 63011335 Tawan Lekngam
# Lab10 Q2

def remove_the_thirds(param: list):
    temp = []
    for i in range(len(param)):
        if (i+1) % 3 != 0:
            temp.append(param[i])
    print(param)
    print(temp)
    param = temp
    print(param)


if __name__ == "__main__":
    list1 = [3, 6, 6, 3, 7, 2, 0, 1, 5, 4, 7, 9]
    remove_the_thirds(list1)
    print(list1)

# a = [1,2,3]
# c = a
# a[:] = [0,0]
# print(c)
# print(a)