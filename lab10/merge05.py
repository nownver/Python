
# def merge(l1,l2):
#     # l3 = l1 + l2
#     # l4 = list(l3)
#     # for i in l4:
#     #     if i.isdigit() == False:
#     #         l3.remove(i)
#     l3 = list(l3)
#     l4 = [int(x) for x in l3]
#     l4.sort()
#     print(l4)

# l1 = input("Enter l1: ")
# ll1 = l1.split()
# l2 = input("Enter l2: ")
# ll2 = l2.split()
# merge(ll1,ll2)


s = input("Enter list1: ")
items = s.split()
list1 = [eval(x) for x in items]
s = input("Enter list2: ")
items = s.split()
list2 = [eval(x) for x in items]

def merge(list1,list2):

    result = list1 + list2
    for i in range(len(result)):
        for j in range(len(result) - 1 - i):
            if result[j] > result[j+1]:
                a = result[j+1]
                result[j+1] = result[j]
                result[j] = a

    # return result

    print("The merged list is ", end = "")
    for e in result:
        print(e, end = " ")


merge(list1,list2)