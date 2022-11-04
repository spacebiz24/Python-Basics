def common(dict1, dict2):
    dict = {}
    for i in dict1:
        if i in dict2:
            if dict1[i] == dict2[i]:
                dict[i] = dict1[i]
    print(dict)
dicta = {"a":1, "b":2, "c":3, "d":4}
dictb = {"a":2, "b":2, "c":3, "d":5}
common(dicta, dictb)