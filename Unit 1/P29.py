#  Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. 
# Sample String : 'abc', 'xyz' 
# Expected Result : 'xyc abz'

str1 = input("Enter String 1: ")
str2 = input("Enter String 2: ")
print(str2[:2] + str1[2:], "", str1[:2] + str2[2:])