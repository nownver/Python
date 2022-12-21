import pickle
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import os

running: bool = True
phonebook: dict[str, str] = dict()
while running:
    print("===== Menu selection =====\n+ Add new contact\n- Remove a contact\nf Find a contact\np Print all contacts\nq Quit\n==========================")
    usin = input("Your choice >> ")

    if usin == '+':
        name = input("Name: ")
        if '@' in name or '%' in name or '$' in name:
            raise Exception("Cannot be added", name)
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

    # elif usin == "s":
    #     try:
    #         book = open("phonebook.txt", "a")
    #         book.write(f"{phonebook}")
    #         book.close()
    #     except KeyError:
    #         print("This cannot be saved")

    elif usin == "s":
        try:
            filenameforWriting = asksaveasfilename()
            # exists 

            outfile = open(filenameforWriting, "wb")
            pickle.dump(f"{phonebook}", outfile)
            outfile.close()
            # infile = open("phonebook.txt", "rb")
            
        except KeyError:
            print("This cannot be saved")

    elif usin == "l":
        try:
            filenameforReading = askopenfilename()
            print("You can read from " + filenameforReading)

            infile = open(filenameforReading, "rb")
            phonebook = pickle.load(infile)
            print(pickle.load(infile))
            infile.close()
            # infile = open("phonebook.txt", "rb")
            
        except:
            print("This cannot be Loaded")

    # elif usin == "s":
    #     try:
    #         outfile = open("phonebook.txt", "wb")
    #         pickle.dump(f"{phonebook}", outfile)
    #         outfile.close()
    #         # infile = open("phonebook.txt", "rb")
            
    #     except:
    #         print("This cannot be saved")

    elif usin == "p":
        # for k, v in phonebook.items():
        #     print(f"Name: {k:<7} Phone No.: {v:<10}")
        print(f"{phonebook}")
    elif usin == 'q':
        running = False
        print("Good bye.")

    else:
    #     # print(f"{5/0}")
        raise Exception("Command not avaliable", usin)
    #     KeyError
            
