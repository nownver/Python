
s1 = set([1,2,3])
s2 = set(['p', 'q'])
s3 = set(['a', 'b', 'c'])

def product(*param):
    result = []

    # flag = True
    # while flag:

    for i in range(len(param) - 1):
        param = list(param)
        print(param)
        print(param[i])

        for j in range(len(param)):
            param[j] = list(param[j])

        print(type(param[i]))
        print(param)

        for j in range(len(param[i])):
            # print("a")

            # if i+1 == len(param) - 1:
            #     return result
   
            for k in range(len(param[i+1])):
                # print('b')
                t = []
                t.append(param[i][j]) 
                t.append(param[i+1][k])
                result.append(t)
                # print(t)
                print(result)

            # if i+1 == len(param) - 1:
            #     return result
        


    return result


print(product(s1, s2, s3))



# param = set([1,2,3])
# param2 = set(['p', 'q'])

# param = list(param)
# param2 = list(param2)
# # b = list(param2)
# print(type(param))
# result = []
# for j in range(len(param)):
#     # print(type(param))
#     for k in range(len(param2)):
#         t = []
#         t.append(param[j])
#         t.append(param2[k])
#         result.append(t)
# print(result)
