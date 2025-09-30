grocery_list = {}

while True:

    try:
        item = input("").upper().strip()

        if item:
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1

    except EOFError:
        sorted_list = sorted(grocery_list.items())
        for key, value in sorted_list:
            print(f"{value} {key}")
        break
