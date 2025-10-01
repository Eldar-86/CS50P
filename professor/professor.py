import random


def main():
    level = get_level()
    score = 10
    for _ in range(10):
        a = generate_integer(level)
        b = generate_integer(level)
        counter = 2
        result = a + b
        while counter >= 0:
            try:
                answer = int(input(f"{a} + {b} = "))
                if answer != result and counter > 0:
                    counter -= 1
                    print("EEE")
                elif answer != result and counter == 0:
                    counter += 2
                    score -= 1
                    print(f"EEE\n{a} + {b} = {result}")
                    break
                else:
                    break
            except ValueError:
                counter -= 1
                print("EEE")
            if counter < 0:
                score -= 1
                print(f"{a} + {b} = {result}")
                break
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        start, end = 0, 9
    elif level == 2:
        start, end = 10, 99
    else:
        start, end = 100, 999
    return random.randint(start, end)


if __name__ == "__main__":
    main()
