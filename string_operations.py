from posixpath import split
import string

string="Hello I am Karnsinh"

'''
H e l l o[space]I[space]a m[space]K  a  r  n  s  i  n  h
0 1 2 3 4   5   6   7   8 9   10  11 12 13 14 15 16 17 18
'''
'''
We Can User User define string by 
string=input("Enter the String")
'''
print(string)

#Finding Length of string
print("Lenght of given string is ",len(string))

#String Slicing
print("Showing 1st 10 characters of given string:- ",string[0:10])#string[:10] 0-include 10 exclude
print("Showing index 2 to 7 of given string:- ",string[2:8])
print("To show all characters of given string before index 9 ",string[:9])#ind 9 is excluded
print("Printing all characters by gap of 2 starting from index 2 ",string[2:20:2])#string[2::2], string_name[including:excluding:gap]
print("Reversing the string by Negative Indexing ",string[::-1])#index of last character of string is always -1

#Other Functions
str1="I am python programmer"
print("\n",str1)
#string_name.endwith("str_want_to_check")
print("To check string is ending with 'xyz' or not:- ",str1.endswith("xyz"))
print("To check string is ending with 'mmer' or not:- ",str1.endswith("mmer"))
print("To check string is ending with 'mMer' or not:- ",str1.endswith("mMer"))

#string_name.count("char/str")
print("Counting Number of 'p' in given string:- ",str1.count('p'))
print("Counting Number of 'P' in given string:- ",str1.count('P'))

#string_name.find("char/str")
print("To find 'Ram' in given string:- ",str1.find("Ram"))
print("To find 'thon p' in given string:- ",str1.find("thon p"))
print("To find 'am' in given string:- ",str1.find("am"))#showing starting index

#string_name.repalce("char/str","new char/str")
print("Replacing programmer with artist:-",str1.replace("programmer","artist"))#New string is created here old is not replaced
print(str1)

#Upper and Lower Cases
print("Coverting whole string in upper case:-",str1.upper())
print("Coverting whole string in lower case:-",str1.lower())

#Stripping operations
str2="****123456####"
print("\n",str2)
print("Removing '#' from given string:- ",str2.strip("#"))
print("Removing '*' from given string:- ",str2.strip("*"))

print("\n\n\n\t=========The End Thanx for Visiting=========")