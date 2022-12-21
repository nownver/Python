filename = input("Enter a file name: ")
try:
    old = input("Enter the old string ")
    new = input("Enter the new string ")
    if old == new:
        raise Exception
except:
    print("Same old-new", old)

try:
    infile = open(filename, "r")

    context = infile.read()

    if old in context:
        context = context.replace(old, new)

    outfile = open(filename, "w")
    outfile.write(context)
    outfile.close()

    print("DONE")
except FileNotFoundError:
    print("This cannot be opened")
# except FileNotFoundError:
#     print("This cannot be opened")


# infile = open(filename, "rb")
# context = pickle.load(infile)
# print(context)
# infile.close()