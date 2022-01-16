from tkinter import N
from tracemalloc import start


print("To Find Prime ")
starting=int(input("Enter Starting Number:- "))
ending=int(input("Enter last Number:- "))
print(f"\nThe Prime numbers between {starting} and {ending} are ")
for num in range(starting,ending+1):
    if num>1:
        for i in range(2,num):
            if (num%i==0):
                break
        else:
            print(num)
