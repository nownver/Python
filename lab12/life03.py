class Name(object):
    def __init__(self, title, firstName, lastName):
        self.title = title
        self.firstName = firstName
        self.lastName = lastName

    def setName(self,t,f,l):
        self.title = t
        self.firstName = f
        self.lastName = l

    def getFullName(self):
        return f"{self.title}.{self.firstName} {self.lastName}"

class Date(object):
    def __init__(self, day, month, year):
        if 1 <= day <= 31:
            self.day = day
        else:
            raise ValueError("Invalid date")

        if 1 <= month <= 12:
            self.month = month
        else:
            raise ValueError("Invalid month")

        self.year = year

    def setDate(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y

    def getDate(self):
        return f"{self.day}/{self.month}/{self.year}"

    def getDateBC(self):
        return f"{self.day}/{self.month}/{self.year + 543}"

class Address(object):
    def __init__(self, houseNo, street, district, city, country, postcode):
        self.houseNo = houseNo
        self.street = street
        self.district = district
        self.city = city
        self.country = country
        self.postcode = postcode

    def setAddress(self, houseNo, street, district, city, country, postcode):
        self.houseNo = houseNo
        self.street = street
        self.district = district
        self.city = city
        self.country = country
        self.postcode = postcode

    def getAddress(self):
        return f"houseNo:{self.houseNo}\nstreet{self.street}\ndistrict:{self.district}\ncity:{self.city}\ncountry:{self.country}\npostcode:{self.postcode}"

class Department():
    def __init__(self, description, manager,employeelist=[]):
        self.description = description
        self.manager = manager
        self.employeelist = employeelist

    def addEmployee(self, e):
        self.employeelist.append(e)
        e.department = self.description

    def deleteEmployee(self,e):
        self.employeelist.pop(e)
        e.department = None

    def setManager(self, e):
        if e in self.employeelist and isinstance(e, PermEmployee):
            self.manager = e
        else:
            print("not employee")

    def printInfo(self):
        print(f"{self.description}\nmanager:{self.manager}\nemployee:{self.employeelist}")

# class Employee(Person)

class Person(object):
    def __init__(self, title, firstName, lastName, day, month, year, houseNo, street, district, city, country, postcode):
        self.name = Name(title, firstName, lastName)
        self.birthday  = Date(day, month, year)
        self.address = Address(houseNo, street, district, city, country, postcode)

    def printInfo(self):
        print(self.name.getFullName())
        print(self.birthday.getDate())
        print(self.address.getAddress())

class Employee(Person):
    def __init__(self, title, firstName, lastName, day, month, year, houseNo, street, district, city, country, postcode, startDate, department):
        super().__init__(title, firstName, lastName, day, month, year, houseNo, street, district, city, country, postcode)

        self.startDate = startDate
        self.department = department

    def printInfo(self):
        return super().printInfo()

class TempEmployee(Person):
    def __init__(self, title, firstName, lastName, day, month, year, houseNo, street, district, city, country, postcode, wage):
        super().__init__(title, firstName, lastName, day, month, year, houseNo, street, district, city, country, postcode)

        self.wage = wage

    def printInfo(self):
        return super().printInfo()

class PermEmployee(Person):
    def __init__(self, title, firstName, lastName, day, month, year, houseNo, street, district, city, country, postcode, salary):
        super().__init__(title, firstName, lastName, day, month, year, houseNo, street, district, city, country, postcode)

        self.salary = salary

    def printInfo(self):
        return super().printInfo() 