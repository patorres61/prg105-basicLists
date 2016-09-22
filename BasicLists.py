# Phyllis Torres
# Using basic lists to accept user input, sort it, and change it to title case

# Create an empty list of cars and intialize variable to check user input
cars = []
savecar = ""

# describe the program and print instructions for the user
print ('This program will accept user input until the user enters the word: done. When the word done is entered, the' +
       ' list of user input will be sorted into alphabetic order and changed to title case.')
print ('\nInstructions: Enter types of cars, for example,  toyota 4runner or honda civic. Do not worry about' +
       ' capitalizing your input, as the program will take care of that for you. ')
print ('\nWhen you are finished, enter the word: done.')

# begin accepting input and check for the word "done"
while savecar != "done":
    savecar = raw_input('Please enter a type of car: ')
    if savecar != "done":       # if the word is "done", do not append it to the list
        cars.append(savecar)

# sort user input
cars.sort()

print ('\nHere is your list of cars:')
# print list out line by line
for auto in cars:
    print(auto.title())
print ('\n')

