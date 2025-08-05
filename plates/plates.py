def main():
    plate = input("Plate: ").strip().replace(" ", "").upper() #Added strip, replace, and upper to anticipate the user entries
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 2<=len(s)<=6: #Check if plate has a min of 2 and max of 6 char
        return False

    if not s[0:2].isalpha(): #Check if first 2 chars are alpha
        return False

    for i in s: #Check if all chars in plate are either alpha or digit
        if not (i.isalpha() or i.isdigit()):
            return False

    for char in s: #If first digit in string is 0, return false
        if char.isdigit():
            if char == "0":
                return False
            break

    found_digit = False #To check if all chars after the first digit are also digits - It actually took me a while to create this loop, so notes below are for me
    for char in s: #Loop through the string
        if char.isdigit(): #This will find the first digit in string, if any.
            if found_digit: #For any subsequent digits found in the str...
                continue #... just go to the next char in the str (looping)
            found_digit = True #Otherwise, if it's the first digit, switch found_digit to True
        elif found_digit: #If found_digit is true, and a subsequent char is not a digit...
            return False #... return False

    return True


main()
