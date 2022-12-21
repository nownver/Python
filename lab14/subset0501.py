# def subset_sum(seq, target):
#     if target == 0:
#         return True

#     for i in range(len(seq)):
#         if subset_sum(seq[:i] + seq[i+1:], target - seq[i]):
#             return True
#     return False

# print(subset_sum([1,2,3,4], 5))

def subset(lst):
    if len(lst) == 1:
        return [lst]
    res = []
    for sub in subset(lst[0:-1]):
        res.append(sub)
        res.append([lst[-1]])
        res.append(sub+[lst[-1]])
    return res

def subset_sum(lst):
    flag = 0
    # tong = 0
    for i in lst:
        if sum(i) == 0:
            flag += 1
            if flag ==1:
                print("yes", end="")
            print(tuple(i), end="")
    if flag == 0:
        print("no")
            

a = subset([-7,4,5])
subset_sum(a)

# print(subset_sum([-7,-3,-2,5,7]))

