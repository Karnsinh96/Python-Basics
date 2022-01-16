
num=int(input("Please Enter The Number "))
fact=1
if num==1:
    print(f"Factorial of {num}is 1")
elif(num>1):
    for i in range(1,num+1):
        fact=fact*i
        i=i+1
    print(f"Factorial of {num} is {fact}")
else:
    print("Please Enter Positive Number Only")