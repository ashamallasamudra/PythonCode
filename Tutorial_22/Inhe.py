#Super()invoke class mehtod 
class A():
    def m1(self):
        print("this is parent class")
class B(A):  #acquring rpop from parent class
    def m2(self):
        print("this is child class")
        super().m1()
bobj=B() 
bobj.m2() 
# Super()invoke class Variable
class A():
    x,y=1,2
class B(A):   
    i=100
    j=200 
    def m1(self,a,b):
        print(a+b)
        print(self.x+self.y)
        print(self.i+self.j)
b=B()
b.m1(10,20)
class A():
    def m1(self):
        print("this is parent class")
class B(A):  #acquring rpop from parent class
    def m2(self):
        print("this is child class")
        super().m1()
bobj=B() 
bobj.m2() 
#Super()invoke class Variable with same var name 
a,b=100,200
class A():
    a,b=1,2
class B(A):   
  a,b=1000,2000
  def m1(self,a,b):
    print(a+b)#invoke method variable
    print(self.a+self.b)#invoke child class variable
    print(super().a+super().b)
        #invoke parent class variable using super bec of same var name
    print(globals() ['a']+globals() ['b'])#invoke Global class variable

bobj=B()
bobj.m1(10,20)
#Super()invoke constructors
class A():
    def __init__(self):
        print("This is parent constructor")
class B(A):
    def __init__(self):
        print("This is child constructor")
        super().__init__()
        A.__init__(self)
b=B()
