#--------------------self-----------------------
def get_the_dif(l1, l2):
    lst = []
    for i in l1:
        if i not in l2:
            lst.append(i)

    for i in l2:
        if i not in l1:
            lst.append(i)

    print(lst)
get_the_dif([3,1,1,1,2,7],[4,1,1,2,2,5])

#----------------jeff--------------------

# def get_the_dif(l1, l2):
#     new = [x for x in l1 if x not in l2]
#     new.extend(x for x in l2 if x not in l1)
#     print(new)
# get_the_dif([3,1,1,1,2,7],[4,1,1,2,2,5])

#-----------------senior------------------------
# l6 = []
# def get_the_differ(l1,l2):
#     for i in range(len(l1) if len(l1)>len(l2) else len(l2)):
#         if l1[i] not in l2 and l2[i] not in l1:
#             l6.append(l1[i])
#             l6.append(l2[i])

#     print(l6)

# get_the_differ([1,2,3,5],[1,2,3,6])

#--------work but not pass-----------------
# def get_the_dif(l1:list,l2:list):
#     d = dict()
#     l3 = l1+l2
#     l5 = []
#     l4 =[]
#     print(l3)
#     for i in range(len(l3)):
#         if i in l1 and i in l2:
#             l5.append(i)
#         d[l3[i]] = l3.count(l3[i])

#     for k,v in d.items():
#         l4.append(k)
#         print(k)

#     print(l4)
# get_the_dif([3,1,1,1,2,7],[4,1,1,2,2,5])

