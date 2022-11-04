dict = {"a":1, "b":2, "c":1, "d":4, "e":3}
def count_values(diction):
    val_list = []
    val_list = list(diction.values())
    count = 0
    new_list = []
    for ele in val_list:
        if ele not in new_list:
            count += 1
            new_list.append(ele)
    print("Unique Elements are: ", count)
count_values(dict)