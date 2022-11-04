list = ["Apple", "Orange", "Banana", "Kiwi"]
for j in range(len(list)):
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            list[i], list[i + 1] = list[i + 1], list[i]
print("Sorted List is:")
print(list)