####import time
####sec = int(input('sec='))
####class convert:
####    def __init__(self,sec):
####        self.sec=sec
####class otvet(convert):
####    def ff(self):
####        ty_res = time.gmtime(sec)
####        print(time.strftime("%H:%M:%S",ty_res))
####gg=otvet(sec)
####gg.ff()
##sec = int(input('sec='))
##class convert:
##    def __init__(self,sec):
##        self.sec=sec
##class lox(convert):
##    def kk(self):
##        print(sec // 60)
##hh=lox(sec)
##hh.kk()
##a=('a',6,7,3)
##print(a)
##print(a[1])

##a=int(input('a='))
##b=int(input('b='))

##class calc:
##    def __init__(self,a,b):
##        self.a=a
##        self.b=b
##    def prover(self):
##        try:
##            b=0
##            c=a/b
##        except ZeroDivisionError:
##            print('hhh')
##gg=calc(a,b)
##
##gg.prover()

##a=str(input('a='))
##s=int(input('s='))
##print(a*s)
##a=[]
##n=list(input('n='))
##a.appened(n)
##
##while True:
##    if n !=0:
##        print(a.reverse())
##    else:
##        print(a)



##a = []
##n=int(input('n='))
##for i in range(n):
##    a.append(i)
##while True:
##    if n !=0:
##        print(a.reverse())
##    else:
##        print(a)
age=int(input('age='))
class cheker:
    def __init__(self,age):
        self.age=age
    def cheker1(self):
        if age <= 19:
            print('idi domoi shkolota')
        elif age <=40:
            print('muzik')
        elif age>=40:
            print('dedugan')
ff=cheker(age)
ff.cheker1()
