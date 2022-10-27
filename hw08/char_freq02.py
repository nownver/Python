
percent = dict()
input_string = input("Enter some text: ")

for c in input_string:
    char_count = input_string.count(c)
    percent[c] = (char_count/len(input_string))*100

for i in percent:
    print(f"{i}{'{:.2f}'.format(percent[i]):>10}%")


# for i,j in enumerate(percent):
#     print(f"{j}\t{percent[i]}%")
