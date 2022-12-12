# Design and implement a python program to create and read a file, store it in a list of lists, with each inner list containing the product name, net weight and the unit price of a product, by name shopper_list.txt that contains the name, weight and the unit price of the products in supermarket:
# Wheat flour 1kg 25.00
# Rice flour 1kg 40.00

file = open("Unit 3/shopper_list.txt", 'w')
num = int(input("Enter number of items: "))
for i in range(num):
    file.write(input("Enter name of item: "))
    file.write(",")
    file.write(input("Enter weight of item: "))
    file.write(",")
    file.write(input("Enter unit price of item: "))
    file.write("\n")
file.close()

file = open("Unit 3/shopper_list.txt", 'r')
list = file.readlines()
Item = []
for line in list:
    word = line.split(",")
    Item.append(word)
print(Item)
file.close()