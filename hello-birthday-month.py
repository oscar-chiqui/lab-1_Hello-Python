# Oscar Chiqui -  ITEC 2905-80 Software Development Capstone 

# https://docs.python.org/3/library/datetime.html

from datetime import date

today = date.today()

print("Today's date:", today)


#Current Python version 

print("Python Version: 3.11.1")

# https://www.w3schools.com/python/ref_string_title.asp 

# Program title to explain about the content
# string.title()

txt = "Hello, Birthday Month Program "
x = txt.title()
print(x)

name = input("What's your name ?  ")
birth_Month = input("What month were you born ? ")

print("Hello" + name + "!")

# A message with the number of letters in your name

count = len(str(name))

print("There are " + str(count) + " characters in your name!")

# The current month 

if birth_Month == "January":
    
    print("Happy birthday month!")