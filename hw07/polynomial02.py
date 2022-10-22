
class Poly():

    def __init__(self, numbers):
        self.numbers = numbers
   
    def add(self, other):
        sum = 0
        result = []

        if len(self.numbers) >= len(other.numbers):
            for i in range(len(self.numbers)):
                if i >= len(other.numbers):
                    sum = self.numbers[i]
                else:
                    sum = other.numbers[i] + self.numbers[i]
                result.append(sum)
        else:
            for i in range(len(other.numbers)):
                if i >= len(self.numbers):
                    sum = other.numbers[i]
                else:
                    sum = other.numbers[i] + self.numbers[i]
                result.append(sum)
        return Poly(tuple(result))

    def scalar_multiply(self, n):
        scl_mut = 0
        result = []

        for num in self.numbers:
            scl_mut = num * n
            result.append(scl_mut)
        return Poly(tuple(result))

    def multiply(self, p):
        base = 0
        expo = 0
   
        n = (len(p.numbers)) + (len(self.numbers)) - 1
        result = [0 for col in range(n)]
        for i, j in enumerate(self.numbers): 
            for k, l in enumerate(p.numbers):
                base = j * l 
                expo = i + k
                result[expo] = base + result[expo]

        return Poly(tuple(result))

    def power(self, n):
        self_poly = Poly(self.numbers)
        if n >= 0:
            for i in range(n-1):
                self_poly = self_poly.multiply(self_poly)
        return self_poly

    
    def diff(self):
        base = 0
        expo = 0
        
        result = []
        for i, j in enumerate(self.numbers):
            base = i * j
            expo = i - 1
            result.insert(expo, base)
        return Poly(tuple(result))

    def integrate(self,n):
        base = 0
        expo = 0
         
        result = []
        for i, j in enumerate(self.numbers):
            expo = i + 1
            base = j / expo
            result.insert(expo, base)
        return Poly(tuple(result))

    def eval(self, n):
        sum = 0
        result = 0
        for i, j in enumerate(self.numbers):
            sum += (j * (n ** i))
        result = sum

        print(result)

    def print(self):
        result = ""
        list_of_num = []
        for i, j in enumerate(self.numbers):
            result = str(j) + 'x' + '^' + str(i)
            if i == 1:
                result = str(j) + 'x'
            if i == 0:
                result = str(j)
            if j == 0:
                result = ''
            list_of_num.append(result)

        for i in range(len(list_of_num)):
            if len(list_of_num[i]) == 0:
                continue
            sign = '+' if i != 0 and list_of_num[i][0] != '-' else list_of_num[i][0]

            print(f"{sign}",end = "")
            print(f" {str(list_of_num[i]) if sign == '+' else str(list_of_num[i][1:])} ",end = "")
   

p = Poly((1, 0, -2))
p.print()

print("")

q = p.power(1)
q.print()
print("")
# j = p.power(3)
# j.print()

print("")

p.eval(3)

r = p.add(q)
r.print()

print("")

r.diff().print()

