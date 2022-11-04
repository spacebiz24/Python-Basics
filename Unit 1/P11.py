cc = int(input("Enter number of credits earned: "))
if cc >= 90:
    print("Senior Status")
elif cc >= 60:
    print("Junior Status")
elif cc >= 30:
    print("Sophomore Status")
else:
    print("Freshman Status")