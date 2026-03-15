a=10
if a>20:
    print("conditon is true")
else:
    print("conditon is false")



a=10
if a>5:
    print("conditon is true")
else:
    print("conditon is false")

#if->executes True/1 , else-->executes False/0
a=10
if True:
    print("conditon is true")
else:
    print("conditon is false")


a=10
if False:
    print("conditon is true")
else:
    print("conditon is false")


a=10
if 1:
    print("conditon is true")
else:
    print("conditon is false")


a=10
if 0:
    print("conditon is true")
else:
    print("conditon is false")

#Even and odd
a=20
if a%2==0:
    print("even number")
else:
    print("odd number")

a=25
if a%2==0:
    print("even number")
else:
    print("odd number")

#Multiple statements under if else blocks
if True:
    print("statement1")
    print("statement2")
    print("statement3")
else:
    print("statement4")
    print("statement5")
print("----------------------------------------------------------------")
if False:
    print("statement1")
    print("statement2")
    print("statement3")
else:
    print("statement4")
    print("statement5")
print("----------------------------------------------------------------")
if False:
    print("statement1")
    print("statement2")
    print("statement3")
else:
    print("statement4")
    print("statement5")
print("i am not part of blocks")

#Single line statement
print("welcome") if True else print("python")
print("welcome") if False else print("python")
print("welcome") if 10>2 else print("python")
print("welcome") if 10<2 else print("python")

print("----------------------------------------------------------------")
#Multi line statement
{print("welcome"),print("welcome1")} if True else {print("python"),print("python1")}
{print("welcome"),print("welcome1")} if False else {print("python"),print("python1")}
print("----------------------------------------------------------------")

#elif
a=4
if a==20:
    print("Twenty")
elif a==30:
    print("Thirty")
elif a==4:
    print("Four")
#else optional
else:
    print("Not listed")


