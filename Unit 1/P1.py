# Design and implement a program
# 1) To prompt the user for hours ad rate per hour to compute gross pay
# 2) To print the python version that is used.

import sys

rph = float(input("Enter the Rate per Hour: "))
h = float(input("Enter the number of hours: "))
gp = rph * h
print("Gross Pay is: ", gp)
print("System Version is: ", sys.version)