#lambda functions
x=lambda a:a+10
print(x(9))
x=lambda a,b:a+b
print(x(1,2))
x=lambda a,b,c:a+b+1
print(x(1,2,3))

def add(a,b):
   x=a+b
   return x
print(add(5,6))

def add(a):
   a=a+10
   return a
print(add(25))