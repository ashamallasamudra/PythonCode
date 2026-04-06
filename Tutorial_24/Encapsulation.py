# private varibles can be accessed  within thew same classs not outside the  class
# class myclass():
#     __a=100 #-->indicates __ private
#     def m1(self):
#         print(self.__a)
# m=myclass()
# m.m1()
#print(myclass__a)
# private methods can be accessed only within the method
class myclass():
    def __m1(self):
        print("this is m1 private method")
    def m2(self):
        print("this is m2 method")
        self.__m1()
mobj=myclass()
    #m.__m1()
mobj.m2()