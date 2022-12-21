
def list_reverse(lst):
    if len(lst) == 0: 
        return []
    return [lst[-1]] + list_reverse(lst[:-1])

print(list_reverse([1,2,3]))

a = [1, 2, 3]
print([a[-1]]+ a[:-1])