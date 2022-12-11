# Write a function called dict_intersect that takes two dictionaries as arguments and returns a dictionary that contains only the key/value pairs found in both of the original dictionaries.

def dict_intersect(dict1, dict2):
    dict = {}
    for i in dict1:
        if i in dict2:
            if dict1[i] == dict2[i]:
                dict[i] = dict1[i]
    print(dict)
dicta = {"a":1, "b":2, "c":3, "d":4}
dictb = {"a":2, "b":2, "c":3, "d":5}
dict_intersect(dicta, dictb)