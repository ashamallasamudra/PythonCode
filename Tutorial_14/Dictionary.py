#Creating Dic
colours={'red':1,'blue':2}
print(colours)
#Retiving
print(colours['red'])
print(colours['blue'])
#Adding elements into dict
colours['pink']=3
print(colours)
#Modifying elements
colours['pink']=5
print(colours)
#Deleting
del colours['pink']
print(colours)

#looping into dictionary
colours= {'a':'red',
          'b':'blue',
          'c':'green'
          }
for i in colours:
    print(i, ":" ,colours[i])
#finding length in dictionary
print(len(colours))


#==and!= operators in dictionary
a1={'a':'apple','b':'ball'}
b1={'b':'apple','a':'ball'}
print(a1==b1)
a1={'a':'apple','b':'ball'}
b1={'b':'apple','a':'ball'}
print(a1!=b1)
a1={'a':'apple','b':'ball'}
b1={'b':'ball','a':'apple'}
print(a1==b1)
a1={'a':1,'b':4}
b1={'b':4,'a':1}
print(a1==b1)
#Dict methods
print(colours)
print(colours.popitem())
print(colours)
#print(colours.clear())
print(colours.keys())
print(colours.values())
print(colours.get('a'))
print(colours.get('blue'))
print(colours.pop('a'))
print(colours.pop('b'))
print(colours)