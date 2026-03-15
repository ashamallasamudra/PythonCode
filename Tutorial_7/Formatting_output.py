#Approach 1
Name='John'
age=27
salary=50000.45
print(Name,age,salary)

#Approach 2
print("Name is",Name)
print("age is",age)
print("salary is",salary)


#Approach 3 using % here type is important exact match
print("Name:%s, age:%d , salary:%f" %(Name,age,salary)) 

#Approach 4 here value is important
print("Name:{}, age:{}, salary:{}".format(Name,age,salary))

#Approach 5 here indexing
print("Name:{0}, age:{1}, salary:{2}".format(Name,age,salary))


#type errors
#print("Name:%s, age:%d , salary:%f" %(age,Name,salary)) 

# changing values 
print ("Name:{},age:{},salary:{}".format(age,age,age))

# choice on indexing
print("Name:{2},age:{2},salary:{0}".format(Name,age,salary))