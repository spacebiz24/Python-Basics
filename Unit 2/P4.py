def checkcommon(lst1, lst2):
    for i in lst1 and lst2:
        if i in lst1 and lst2:
            return "True"
    return "False"
print(checkcommon([1,2,3], [4,5,6]))