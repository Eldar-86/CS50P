import random

while True:
    try:
        lvl_choice = input("Level: ")
        lvl_choice = int(lvl_choice)
        random_number = random.randint(1, lvl_choice)
        break
    except ValueError:
        continue
    except EOFError:
        print("Alright -- quitting.")
        break

while True:
    try:
        user_input = input("Guess: ")
        user_input = int(user_input)
        if user_input>0:
            if user_input < random_number:
                print("Too small!")
                continue
            elif user_input > random_number:
                print("Too large!")
                continue
            else:
                print("Just right!")
                break
        else:
            continue
    except ValueError:
        continue
    except EOFError:
        print("Alright -- quitting.")
        break


##Another nice feature would be to introduce a 'try counter' based on the level chosen, so there are a limited number of tries to guess the number
