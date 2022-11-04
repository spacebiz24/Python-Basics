print("Format of entering Details:")
print("Name,USN,Semester")
x = input("Enter Student Details: ")
lst = []
lst = x.split(",")
lst[1] = lst[1].upper()
lst[2] = int(lst[2])
print(lst)