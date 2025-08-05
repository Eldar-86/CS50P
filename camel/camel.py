string = input("$ ") #Collect user input as str
new_string = "" #Create a new empty str which will be populated via str iteration

for s in string: #Iterating through the str
    if s.isupper(): #This condition is to update new str for an upper case char
        new_string += "_" + s.lower()
    else: #This condition is to update new str for a lower case char
        new_string += s

print(new_string) #Print the new and updated str
