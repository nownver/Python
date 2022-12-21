

# def powerSet(items):
#     # generate all combinations of N items, items is a Python list
#     N = len(items)
#     # enumerate the 2**N possible combinations
#     for i in range(2**N):
#         combo = []
#         for j in range(N):
#             # test bit jth of integer i
#             if (i >> j) % 2 == 1:
#                 combo.append(items[j])
#         return combo


#-------------------------pTawan---------------------------
# 63011335 Tawan Lekngam
# Lab11 Q5

def power(param: set):
    subsets: list[frozenset] = [frozenset()]
    for ele in param:
        for i in range(len(subsets)):
            subset = list(subsets[i])
            subsets.append(frozenset(subset + [ele]))
    return (subsets)

if __name__ == "__main__":
    s = set([1,2,3])
    print(power(s))
