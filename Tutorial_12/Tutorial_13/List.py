# #List
# list1=list()
# print(list1)#empty string
# list2=list([1,2,3,4])
# print(list2)#list of no
# list3=list(['oil','salt','spicy','water'])
# print(list3)#list of strings
# list4=list("python")
# print(list4)#list of a charcter
# #Accessing element in the string
# l1=[1,2,3,4]
# print(l1[0])
# print(l1[3])
# print(l1[-1])
# print(l1[-2])
# #in and not in operators
# lis=[3,5,7,9]
# print(3 in lis)
# l=[3,5,7,9]
# print(3 not in lis)
# l=[3,5,7,9]
# print(11 in lis)
# #len, min max sum 
# l1=[23,22,21,24,25]
# print(min(l1))
# print(max(l1))
# print(sum(l1))
# print(len(l1))
# #Slicing Operators
# l2=[2,3,4,3]
# print(l2[1:2])
# print(l2[:-1])
# print(l2[-1])
# #Traversing list using for loop
# le=[9,1,7,9,6,5]

# for i in le:
#     print(i)
# for i in le:
#     print(i, end=" ")
# print("-----------------")  
# #operators in list + and *
# li=[8,7,1,5]
# lo=[1]
# lk=li+lo
# print(lk)
# print(li+lo)
# print(lo*5)
list=[1,2,3,4]
list.append(9)
list.append(9)
print(list)
print(list.count(9))
list1=[1,2,3]
list2=[3,4]
list1.extend(list2)
print(list1)
print(list1.index(2))
print(list1.index(3))
list1.remove(3)
print(list1)
list1.remove(3)
print(list1)
list1.reverse()
print(list1)
#List_Comperhension
l1=[x for x in range(10)]
print(l1)
l1=[x+1 for x in range(10)]
print(l1)

#Even no x in range(10)]
l1=[x for x in range(10) if x%2==0]
print(l1)