def DectoBin(num):
    if num >= 1:
        DectoBin(num // 2)
    print(num % 2, end = "")

DectoBin(10)