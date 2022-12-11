# Write a program to read details of the student(name as string ,usn as int ,semester as int) in comma separated values from the keyboard and split & typecast the input based on comma delimiter and store it in list before displaying it.

print("Format of entering Details:")
print("Name,USN,Semester")
x = input("Enter Student Details: ")
lst = []
lst = x.split(",")
lst[1] = lst[1].upper()
lst[2] = int(lst[2])
print(lst)