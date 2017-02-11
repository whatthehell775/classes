class fraction:

    def __init__(self,top,bottom):

        self.nu=top
        self.den=bottom

    def show(self):

        print self.nu,"/",self.den

    def __str__(self):
        return str(self.nu)+'/'+str(self.den)

    def float_d(self):

        return float(self.nu)/float(self.den)

    def int_d(self):

        return int(self.nu)/int(self.den)

    def __add__(self,ofr):
        
        from fractions import gcd
        nnum = self.nu*ofr.den + ofr.nu*self.den
        nden = ofr.den*self.den
        g = gcd(nnum,nden)
        nnum = nnum/g
        nden = nden/g
        return fraction(nnum,nden)

    def __eq__(self,other):
        f1 = self.nu*other.den
        f2 = self.den*other.nu
        return f1==f2
        
