greeting = input("$ ").split()[0]
greeting1 = greeting.strip().strip("!").strip("?").strip(".").strip("'").strip(",").capitalize()
no_dollar_greeting = ["Hello"]
twenty_dollar_greeting = ["Hi", "Hey", "Hiya", "How", "Hiyya"]

if greeting1 in no_dollar_greeting:
    print("$0")
elif greeting1 in twenty_dollar_greeting:
    print("$20")
else:
    print("$100")
