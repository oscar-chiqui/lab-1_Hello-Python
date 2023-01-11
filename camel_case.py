# Oscar Chiqui -  ITEC 2905-80 Software Development Capstone 

# A program that turns a sentence into camel case.

print("Enter a sentence to convert into a camelCase")
input_sentence = input("> ")


new_word = False
output_sentence = ""      # empty until the output display the sentence 
first_letter = False          # The first word is lowercase

# loop over that string 

#  the elif conditions are applied after the if condition.
# https://www.tutorialsteacher.com/python/python-if-elif 

for char in input_sentence:
    if char == ' ':
        new_word = True

    elif not (char.isalpha() or char.isalnum()):      # The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9)
        print("Invalid character use a letter a-z \'" + char + "\'")

#the rest of the words have their initial letter capitalized, and all of the words are joined together.

    else:    

        if first_letter:
            if new_word is True:
                output_sentence += char.upper()
            else:
                output_sentence += char.lower()

        else: 
            if char.isalpha():
                first_letter = True
                output_sentence += char.lower()
            else:
                
                print("invalid character use a letter a-z  \'" + char + "\'")   

            new_word = False

print("Here is your string in camelCase:")
print(output_sentence)

