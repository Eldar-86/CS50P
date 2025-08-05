"""answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ").capitalize().strip()
acceptable = ["42", "Forty-two", "Forty two"]
if answer in acceptable:
    print("Yes")
else:
    print("No")""" # Still, if input is " forty two " here (and below), output will fail (or be "No", when it should be "Yes"). I guess the solution would be to take the input, remove all spaces, join it by " " between the words and then capitalize it.
                   # Also, we haven't done lists yet, so I will just submit the one with match function

answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ").capitalize().strip()
match answer:
    case "42" | "Forty-two" | "Forty two": print("Yes")
    case _: print("No")
