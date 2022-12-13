# Write a Python class to convert a roman numeral to an integer.

class ConvertToRome:
    def __init__(self):
        self.roman_keys = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    def convert(self, roman):
        sum = prev = 0
        self.roman = roman[::-1]
        for i in range(len(self.roman)):
            if self.roman_keys[self.roman[i]] < prev:
                sum -= self.roman_keys[self.roman[i]]
            else:
                sum += self.roman_keys[self.roman[i]]
            prev = self.roman_keys[self.roman[i]]
        print("Integral Value is: ", sum)

rom = ConvertToRome()
rom.convert("CCXLVIII")