#Strings
str1="piter"
print(str1)
print(id(str1))
str1='joho'
str2="marry"
print(id(str1),id(str2))

#Strings are immutable -->once assigned they are not changable cretadifferent memory location,,,,
str2=str2+"To_Pyhton"
print(str2)
print(id(str2))
#Operatons on string
str="welcome"
print(str+"To_Python")
print(str*8)
str='welcome'
print(str[1:3])#el
print(str[:6])#welcom
print(str[4:])#ome
print(str[1:-1])#elcom

# ord() and char() Functions
print(ord("A"))
print(ord("a"))
print(ord("m"))
print(chr(65))
print(chr(16))#prints invisible character
print("********************************************")
#String functions in python
print(len('welcome'))
print(min('welcome'))
print(max('welcome'))
print(min('Asha'))#A=65,a=97
print(min('sha'))
print("********************************************")
#In and Not in operators
str="Spaces"
print('spa' in str)
print('Spa' in str)
print('spa' not in str)
print('aces' in str)

#String comparision
print("true"=="tru")
print("pen">="ink")
print("laptop"<="desktop")#it check for 1st alpha bet then it is say true /false
print("paper">"Bundel")
print("pen"!="pencil")
 
#Testing string
s='welcome to python'
print(s.isalnum())
s2=''
s1='123nm'
print(s1.isalnum())#true
print(s.isalpha())#because of spaces it is false
s1='12345'
print(s1.isdigit())
print('welco1me'.isidentifier())
print(s.islower())
print(s.isupper())
print('  '.isspace())
print('\t'.isspace())
print('\n'.isspace())

#searching for substring
s='welcome to Python'
print(s.startswith('wel'))
print(s.endswith('thon'))
print(s.find('wel'))
print(s.rfind('o'))
print(s.find('o'))

print(s.startswith('elcome'))
print(s.endswith('to'))
print(s.find('tol'))
print(s.rfind('t'))
print(s.find('t'))

#Converting strings
s='Strings in the Pyhton'
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.replace("Strings","Lists"))
