
input_money = int(input("Enter money: "))
money = input_money
n = 'notes'
if money % 100 == 0:
    if money >= 1000:
        money = money // 1000
        if money == 1:
            n = 'note'
        print(f"You get {money} {n} of 1000 Baths")
        n = 'notes'
    money = input_money % 1000   
    if money >= 500:
        money = money // 500
        if money == 1:
            n = 'note'
        print(f"You get {money} {n} of 500 Baths")
        n = 'notes'
    money = input_money % 500   
    if money >= 100:
        money = money // 100
        if money == 1:
            n = 'note'
        print(f"You get {money} {n} of 100 Baths")
    money = input_money % 100   
else:
    print("none")


 