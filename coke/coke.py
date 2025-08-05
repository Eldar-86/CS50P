amount_due = 50 #Set starting amount
print("Amount due:", amount_due)

while amount_due != 0: #Initiated loop until condition is met -- full payment
    input_amount = int(input("Insert coin: "))

    if input_amount != 25 and input_amount != 10 and input_amount != 5 and input_amount != 0: #Handles accepting only 25c, 10c and 5c
        print("Amount due:", amount_due)
        continue
    else:
        amount_due = amount_due - input_amount

    if amount_due < 0: #Handles change if any
        print("Change owed:", abs(amount_due))
        break
    elif amount_due > 0: #Handles remaining payment
        print("Amount due:", amount_due)
    else: #handles change if none
        print("Change owed:", amount_due)
