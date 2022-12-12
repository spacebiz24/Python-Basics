# Write a program segment that reads a text file named original_text, and displays how many times the letter ‘c’ occurs.

file = open("Unit 3/original_text.txt", 'w')
file.write(input("Enter some text: "))
file.close()

file = open("Unit 3/original_text.txt", 'r')
c_count = 0;
letters = file.read().lower()
for i in range(len(letters)):
    if letters[i] == 'c':
        c_count += 1
print("Numbers of 'c's' are: ", c_count)
file.close()