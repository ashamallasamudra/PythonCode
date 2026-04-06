# #polymorphism
# #overridin the variables
# class parent:
#     name="scott"
# class child(parent):
#     name="david"
# cobj=child()
# cobj.name
# print(cobj.name)
# ###################################
# class parent:
#     name="scott"
# class child(parent):
#    pass
# cobj=child()
# cobj.name
# print(cobj.name)

#############################################
#method overriding
class Bank:
    def rate_of_intrest(self):
        return 0
   
class ICICI(Bank):
   def rate_of_intrest(self):
        return 10

Iobj=ICICI()
print(Iobj.rate_of_intrest())
bobj=Bank()
print(bobj.rate_of_intrest())

#method overloading
class Animals():
    def bites(self,name):
        if name=='dog':
            print("bark")
        if name=='lion':
            print("roars")
        if name==None:
            print("not a animal")
        else:
            print(" a animal")
a=Animals()
a.bites('chita')
a.bites('lion')
        


