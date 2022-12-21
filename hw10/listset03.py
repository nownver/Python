lst1 = [3,1,2,7]
lst2 = [4,1,2,5]

def my_union(l1, l2):
    l3 = l1 + [i for i in l2 if i not in l1]
    return l3

def my_intersect(l1, l2):
    l3 = [i for i in l1 if i in l2]
    return l3

def my_differnce(l1, l2):
    l3 = [i for i in l1 if i not in l2]
    return l3

print(my_union(lst1, lst2))
print(my_intersect(lst1, lst2))
print(my_differnce(lst1, lst2))
