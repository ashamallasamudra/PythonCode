print("hi")

try:
    print(10/0)
except ZeroDivisionError:
    print("Exceptionl handele")
else:
    print("no exception")
finally:
    print("program executes")
print("by")
