# Consider a File Called “workfile”. Write Python Program to Read and Print Each Byte in the Binary File.
file = open("Workfile.jpg", "rb")

for i in file.read(8):
    print(i)

file.close()
