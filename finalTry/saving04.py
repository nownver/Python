class SavingAccount():
    def __init__(self,bank_name , acc_name, acc_id, balance, transaction_history = []):
        self.bank_name = bank_name
        self.acc_name = acc_name
        self.acc_id = acc_id
        self.balance = balance
        self.transaction_history = transaction_history

    def deposit(self, money, person, date):
        self.balance += money
        person.balance -= money
        person.transaction_history.append(f"withdraw {money} by {person.acc_name} to the account on {date}")
        self.transaction_history.append(f"deposit {money} by {person.acc_name} to the account on {date}")

    def withdraw(self, money, person, date):
        if self.money < self.balance:
            self.balance -= money
            self.transaction_history.append(f"withdraw {money} by {person.acc_name} to the account on {date}")
            person.balance += money
            person.transaction_history.append(f"deposit {money} by {person.acc_name} to the account on {date}")
        else:
            print("cannot withdraw")

    def get_balance(self):
        return self.balance

    def print_statement(self):
        for i in self.transaction_history:
            print(i)
        
class OverDrawnAccount(SavingAccount):
    def __init__(self, bank_name, acc_name, acc_id, balance, limit, transaction_history=[]):
        super().__init__(bank_name, acc_name, acc_id, balance, transaction_history)

        self.limit = limit
    
    def withdraw(self, money, person, date):
        self.balance -= money
        if self.balance <= 0:
            self.limit = self.balance
            if self.limit >= 0:
                # self.balance -= money
                self.transaction_history.append(f"withdraw {money} by {person.acc_name} to the account on {date}")
                person.balance += money
                person.transaction_history.append(f"deposit {money} by {person.acc_name} to the account on {date}")
            else:
                self.balance += money 
                print("cannot withdraw")

a = SavingAccount("SCB", "Jeff", "1234", 1000)

# a.deposit(200, a, "10/2")
# print(a.get_balance())
# a.withdraw(1100, a, "10/3")
# print(a.get_balance())
a.print_statement()

b = OverDrawnAccount("KBANK", "Bob", "1234", 20, 200)

b.deposit(100, a, "20/3")
print("aaa")
a.print_statement()
print(a.get_balance())

print(b.get_balance())
b.withdraw(900, b, "10/3")
# print(b.get_balance())
b.print_statement()