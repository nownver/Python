
x1, y1 = eval(input("Enter coordinate 1: "))
x2, y2 = eval(input("Enter coordinate 2: "))
height_1 = eval(input("Enter height 1: "))
height_2 = eval(input("Enter height 2: "))
width_1 = eval(input("Enter width 1: "))
width_2 = eval(input("Enter width 2: "))


# top left 1
a1 = x1 - width_1 / 2
a2 = y1 + height_1 / 2

# top right 1
b1 = x1 + width_1 / 2
b2 = y1 + height_1 / 2

#bottom left 1
c1 = x1 + width_1 / 2
c2 = y1 - height_1 / 2

#bottom right 1
d1 = x1 - width_1 / 2
d2 = y1 - height_1 / 2

#---------------

# # top left 2
e1 = x1 - width_2 / 2
e2 = y2 + height_2 / 2

# top right 2
f1 = x2 + width_2 / 2
f2 = y2 + height_2 / 2

#bottom left 2
g1 = x2 + width_2/ 2
g2 = y2 - height_2 / 2

#bottom right 2
h1 = x2 - width_2 / 2
h2 = y2 - height_2 / 2

# point_list_x = [e1, f1, g1, h1] 
# point_list_y = [e2, f2, g2, h2]

def check_overlap_1(list1):
    for value in list1:
        if a1 < value < b1 :
            truth =  1
        else:
            truth =  0
        return truth

# def check_overlap_2(list2):
#     for value2 in list2:
#         if a1 < value2 < b1 :
#             truth =  1
#         else:
#             truth =  0
#         return truth

# if e1 - f1 < b1 - a1:
#     check_overlap_1(point_list_x) 


    
# if check_overlap_1(point_list_x) == 1 and check_overlap_2(point_list_y) == 1:
#     print("overlap")
# elif 

#efgh smaller than abcd
if f1 - e1 < b1 - a1 and g2 - f2 < c2 - b2 :
    if (a1 < e1 and f1 and g1 and h1 < b1) and (b2 < e2 and f2 and g2 and h2 < c2) :
        print("Inside")
#efgh bigger than abcd
elif f1 - e1 > b1 - a1 and g2 - f2 > c2 - b2 :
    if (e1 < a1 and b1 and c1 and d1 < f1) and (f2 < a2 and b2 and c2 and d2 < g2) :
        print("Inside")
