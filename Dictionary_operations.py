#Creating a Dictionary
myDict1={
            "Name":"Raj",
            "Marks":[10,20,30],
            "Roll_num":101 ,
            "nested_dict1":{"raj":'Also A Player'}
        }
print(myDict1)

#Accessing Keys
print(myDict1.keys())
print(type(myDict1.keys()))

#Accessing Values
print(myDict1.values())
print(type(myDict1.values()))

#Accessing Items
print(myDict1.items())
print(type(myDict1.items()))

#Accessing values of Nested Dictionary
print()
print(myDict1["nested_dict1"]["raj"])

#Updating Dict
myDict2={"Mob_No":9146570570}
print(myDict2)
myDict1.update(myDict2)
print(myDict1)

myDict1["Mob_No"]=9403870906
print(myDict1)

#Deleting the values
print()
employee_dict={101:"Raja",102:"Sunya",103:"Parshya",104:"Anya",105:"Ashya"}
print(employee_dict)
employee_dict.pop(104)
print(employee_dict)
