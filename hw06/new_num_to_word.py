my_dict_1 = {0: 'zero',1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 
             14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
my_dict_2 = {20: 'twenty', 30: 'thirty', 40: 'forty', 50:'fifty', 60: 'sixty',70:'seventy',80:'eighty',90: 'ninety'}


def translate(num):
    str_num = str(num)

    if num in my_dict_1:
        return my_dict_1[num]
    elif num in my_dict_2:
        return my_dict_2[num]
    elif num < 100:
        a = num % 10
        b = (num //  10) * 10
        return my_dict_2[b] + "-" + my_dict_1[a]
    elif num >= 100:
        a = num % 10
        c = num // 100
        b = (num - c * 100) - a
        if num % 100 == 0:
            return my_dict_1[c] + " hundred"
        elif int(str_num[1:]) in my_dict_1:
            return my_dict_1[c] + " hundred and " + my_dict_1[int(str_num[1:])]
        elif int(str_num[1:]) in my_dict_2:
            return my_dict_1[c] + " hundred and " + my_dict_2[int(str_num[1:])]
        else:
            return my_dict_1[c] + " hundred and " + my_dict_2[b] + "-" + my_dict_1[a]

input_num = int(input("Enter a number: "))

if 0 <= input_num <= 999:
    print(translate(input_num))
else:
    print("I don't know.")

