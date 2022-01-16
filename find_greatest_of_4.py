
a=int(input("Enter 1st Number:-\n"))
b=int(input("Enter 2nd Number:-\n"))
c=int(input("Enter 3rd Number:-\n"))
d=int(input("Enter 4th Number:-\n"))

print(f"The Numbers Are {a},{b},{c},{d} ")
if(a>b):
    num1=a
else:
    num1=b

if(c>d):
    num2=c
else:
    num2=d

if(num1>num2):
    print(f"\n{num1} is greatest")
else:
    print(f"\n{num2} is greatest")