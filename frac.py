class fraction:

    def __init__(self,top,bottom):
	self.num=top
        self.den=bottom

    def show(self):
	print self.num,"/",self.den

    def __str__(self):
        return str(self.num)+'/'+str(self.den)

    def float_d(self):
	return float(self.num)/float(self.den)

    def int_d(self):
	return int(self.num)/int(self.den)

    def __add__(self,other):
        from fractions import gcd
        nnum = self.num*other.den + other.num*self.den
        nden = other.den*self.den
        g = gcd(nnum,nden)
        nnum = nnum/g
        nden = nden/g
        return fraction(nnum,nden)

    def __eq__(self,other):
        f1 = self.num*other.den
        f2 = self.den*other.num
        return f1==f2
        
