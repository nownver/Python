class BankAccount():
    def __init__(self, name, owner, acc_num, cur_num):
        self.name = name
        self.owner = owner
        self.acc_num = acc_num
        self.cur_num = cur_num
    
    def deposit(self, depo):
        self.depo = depo
        self.cur_num = self.cur_num + self.depo

    def withdraw(self, wd):
        self.wd = wd
        if self.wd > self.cur_num:
            self.cur_num = self.cur_num
        else:
            self.cur_num = self.cur_num - self.wd
    def print_out(self):
        print(f"{self.cur_num}")


acc1 = BankAccount("ura", "yok", 1111, 200)
acc1.deposit(50)
acc1.withdraw(300)
acc1.print_out()
    





