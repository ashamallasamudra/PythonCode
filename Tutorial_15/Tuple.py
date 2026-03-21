#creating tuples
t1=()
t2=(1,2,3,4,5)
t3=([1,2,3,4])
t4=('a','b')
t5=tuple("Ginger")
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
#Tuple functions
t=(23,2,2333,4343434,33343)
print(min(t))
print(max(t))
print(len(t))
print(sum(t))
#loops
for i in t:
    print(i, end=" ")
print("\n")

#Slicing
tu=(1,2,3,8,9,10,11,12,15)
print(tu[1:3])
print(tu[0:])
print(tu[-1])

#in and not in operators
tu=(8,9,10,11,12,15)
print(9 in tu)
print(9 not in tu)