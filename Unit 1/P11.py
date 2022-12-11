# Write a Python program in which a student enters the number of college credits earned. If the number of credits is greater than 90, 'Senior Status' is displayed; if greater than 60, 'Junior Status' is displayed; if greater than 30, 'Sophomore Status' is displayed; else, 'Freshman Status' is displayed.

cc = int(input("Enter number of credits earned: "))
if cc >= 90:
    print("Senior Status")
elif cc >= 60:
    print("Junior Status")
elif cc >= 30:
    print("Sophomore Status")
else:
    print("Freshman Status")