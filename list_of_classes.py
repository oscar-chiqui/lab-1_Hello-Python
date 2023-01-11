# Oscar Chiqui - # Oscar Chiqui -  ITEC 2905-80 Software Development Capstone

# "The program will display the classes in a list.
# based on the number of classes you take this semester

# The number of classes

the_classes_number = input('How many classes are you taking this semester ?')

# Convert user's entry  to an int to later validate as needed in the program.

class_int = int(the_classes_number)

# the name of the classes will be used in this empty space
class_list = []


# https://www.programiz.com/python-programming/methods/list/append

# based on the number of classes that the user writes, the range will be measured.

for x in range(class_int):
    class_list.append(input('Enter the name of the class: '))

print('Here is the list of your classes for this semester :')

# Print all the items in the list, one per line.
for entry in class_list:
    print(entry)
