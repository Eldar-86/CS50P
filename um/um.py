import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    search = re.findall(r"\bum\b", s, flags=re.IGNORECASE)
    if search:
        word_count = 0
        for _ in search:
            word_count += 1
        return word_count
    else:
        raise ValueError


if __name__ == "__main__":
    main()
