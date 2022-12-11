# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

my_dict = dict()
for i in range(1, 20 + 1):
    my_dict[i] = i ** 2
print("Dictionary:")
print(my_dict)
print("Keys:")
print(list(my_dict.keys()))