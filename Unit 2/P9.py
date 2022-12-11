# Write a Python program to remove duplicates from a list.

list = [1,2,3,3,3,4,5,6]
nlist = []
for i in list:
    if i not in nlist:
        nlist.append(i)
print("New List: ", nlist)