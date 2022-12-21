# book = {}

# while True:
#     press = input("press: ")
#     if press == '+':
#         name = input("name: ")
#         if name in book:
#             print("same name")
#             continue
#         # name = input("name: ")
#         numb = input("number: ")
#         book[name] = numb
#     elif press == '-':
#         name = input("name: ")
#         book.pop(name)
#     elif press == 'f':
#         name = input("name: ")
#         for i in book:
#             if i == name:
#                 print(book.get(name))
#             else:
#                 print("cant find")
#     elif press == 'p':
#         print(book)
#     elif press == 'q':
#         break


#--------------pTawan-------------------
# 63011335 Tawan Lekngam
# Lab11 Q1

running: bool = True
phonebook: dict[str, str] = dict()
while running:
    print("===== Menu selection =====\n+ Add new contact\n- Remove a contact\nf Find a contact\np Print all contacts\nq Quit\n==========================")
    usin = input("Your choice >> ")
    if usin == '+':
        name = input("Name: ")
        if name in phonebook:
            print("This name already exist.")
        else:
            phonebook[name] = input("Phone No.: ")
    elif usin == '-':
        try:
            name = input("Name: ")
            phonebook.pop(name)
            print(f"Remove {name} from phonebook")
        except KeyError:
            print("This name not in phonebook")
    elif usin == "f":
        try:
            name = input("Name: ")
            print(f"Name: {name:<7} Phone No.: {phonebook[name]:<10}")
        except KeyError:
            print("This name not in phonebook")
    elif usin == "p":
        for k, v in phonebook.items():
            print(f"Name: {k:<7} Phone No.: {v:<10}")
    elif usin == 'q':
        running = False
        print("Good bye.")
    else:
        print("Command not avaliable")