from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass


class Tiger(Animal):
   def eat(self):
        print("eats non veg")
class cat(Animal):
    def eat(self):
        print("eats veg")
t=Tiger()
t.eat()
c=cat()
c.eat()

# multiple abs method on abstrct class must implement all methods in all classe
from abc import ABC,abstractmethod
class A(ABC):       #extract ABC
    @abstractmethod  #must for abst 
    def m1(self):
        pass         #abstt method do not pass anything
    @abstractmethod
    def m2(self):
        pass
class B(A):
    def m1(self):
        print("this is m1 mthod")
    #creating only m1 nad clling throuhg eroor we must declare all method from abstr class
    def m2(self):
        print("this is m2 mthod")
b=B()
b.m1()
b.m2()
#Constructor
from abc import ABC,abstractmethod
class A(ABC):       #extract ABC
    def __init__(self,value):
        self.value=value
    @abstractmethod  #must for abst 
    def add(self):
        pass
    @abstractmethod
    def sub(self):
        pass
class B(A):
    def add(self):
        print(self.value+100)
    #creating only m1 nad clling throuhg eroor we must declare all method from abstr class
    def sub(self):
        print(self.value-100)
b=B(100)
b.add()
b.sub()
