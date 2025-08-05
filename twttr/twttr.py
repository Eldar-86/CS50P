user_input = input("$ ") #Collect input from user
vowel = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"] #List of vowels
new_input = "" #New input to append

for chr in user_input: #Iterate through user input and remove any vowels added to the list above
    if chr not in vowel:
        new_input += chr
print(new_input)
