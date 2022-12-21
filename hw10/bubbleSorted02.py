sample = [3,2,9,7,8]

def bubble_sort(lst):
    flag = True
    while flag:
        for i in range(len(lst) - 1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
  
        if lst == sorted(lst):
            break
    return lst

print(bubble_sort(sample))

            

