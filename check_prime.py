num=int(input("Enter The Number:- "))
if (num>1)==True:
    for i in range(2,num):
        if(num%i==0):
            print(f"{num} is not prime")
            break
        else:
            print(f"{num} is prime")
            break
else:
    print("Enter The number greater than 1")
