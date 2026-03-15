#User Input
#any inside input it is treated as string
num1=input("Enter first number:")
num2=input("Enter second number:")
print(num1+num2)

#type casting
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print(num1+num2)

num1=input("Enter first number:")
num2=input("Enter second number:")
print(int(num1) + int(num2))
#Float holds the integer values but intger can not hold float values

num1=input("Enter first Decimal number:")#10.5
num2=input("Enter second Decimal number:")#10
print(float(num1) + int(num2))

#keping float but passsign int value accpted
num1=input("Enter first Decimal number:")#10.5
num2=input("Enter second Decimal number:")#10
print(float(num1) + float(num2))

#keping int but passsign float value not accpted
num1=input("Enter first Decimal number:")#10
num2=input("Enter second Decimal number:")#10.5
print(int(num1) + int(num2))