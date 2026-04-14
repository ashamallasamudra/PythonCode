#Receiving the arguments
def sum(*args):
    s=0
    for i in args:
        s+=i
    print(s)
sum(1,2) 

def sum(*args):
    s=0
    for i in args:
        s+=i
    print(s)
sum(1,2,3,4,5,6,7,8,9,10)

#Sending the arguments:
def my(a,b,c):
    print(a,b,c)
args=[1,2,3]
my(*args)

