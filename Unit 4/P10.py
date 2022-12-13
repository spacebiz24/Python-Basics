# Write a Python class to reverse a string word by word.
# Input string : 'hello .py'
# Expected Output : '.py hello'

class revstring:
    def __init__(self, string):
        self.string = string
    def revString(self):
        nstr = (self.string).split(" ")
        print("Reversed String is:")
        print(" ".join(nstr[::-1]))

rev = revstring("Siddhaanth S Iyer")
rev.revString()