
def print_table(lst):
    for row in lst:
        for column in row:
            print(f"{column:<8}", end = "")
        print("")

print_table([["x","y"], [0,0], [10,10], [200,200]])

print("")

print_table([["ID", "Name", "Surname"], ["001", "Guido", "van Rossum"], ["002","Donald","Knuth"], ["003","Gordon","Moore"]])