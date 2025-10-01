import validators


def main():
    print(validate(input("What's your email address? ").strip()))


def validate(s):
    if validators.email(s):
        return "Valid"
    elif not validators.email(s):
        return "Invalid"
    else:
        raise ValueError


if __name__ == '__main__':
    main()
