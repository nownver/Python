class Poly:
    def __init__(self,p):
        self.p = list(p)

    def add(self,a):
        l = min(len(self.p),len(a.p))
        p = self.p
        for i in range(l):
            p[i]+=a.p[i]
        if(l<len(a.p)):
            for i in range(l,len(a.p)):
                p.append(a.p[i])
        return Poly(tuple(p))
    
    def scalar_multiply(self,n):
        tmp = []
        for i in range(len(self.p)):
            tmp.append(n*self.p[i])
        return Poly(tuple(tmp))
    
    def multiply(self,p2):
        ans = []
        for i in range(len(self.p)+len(p2.p)-1):
            ans.append(0)
        for i in range(len(self.p)):
            for j in range(len(p2.p)):
                ans[i+j] += self.p[i]*p2.p[j]
        return Poly(tuple(ans))
        
    def power(self,n):
        if(n == 0):
            return Poly(tuple([1]))
        elif(n==1):
            return self
        tmp = self
        for i in range(n-1):
            tmp = tmp.multiply(self)
        return tmp

    def diff(self):
        tmp = [0]*(len(self.p)-1)
        for i in range(1,len(self.p)):
            tmp[i-1]+=self.p[i]*i
        return Poly(tuple(tmp))

    def integrate(self):
        tmp = self.p
        tmp.append(0)
        l = len(tmp)
        for i in range(l-1,0,-1):
            tmp[i] = self.p[i-1]/i
        tmp[0]=0
        return Poly(tuple(tmp))

    def print(self):
        ans = ""
        first = True
        for i in range(len(self.p)):
            if self.p[i] == 0:
                continue
            elif i == 0:
                ans += str(self.p[i])
                first = False
            else:
                if(self.p[i]<0):
                    ans+=" - "
                    first = False
                    ans+= str(self.p[i])[1:]+"x"
                elif(not first): 
                    ans+=" + "
                    first = False
                    if(self.p[i]!=1):
                        ans+= str(self.p[i])
                    ans+="x"
                if(i>1):
                    ans+="^"+str(i)
        print(ans)
                







# p1 = Poly((-5,5,1,10,25,3,1,0,0,0,1))
# p1.print()
# p2 = Poly((1,2,3))
# p3 = Poly((1,0,0,1))
# p2 = p2.scalar_multiply(2)
# p2.print()
# p3 = p3.multiply(p2)
# p3.print()

p2 = Poly((1,2,3))
p2.power(4)
p2.print()
# p2.power(3)
# p2.print()

