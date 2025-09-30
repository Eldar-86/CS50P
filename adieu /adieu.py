name_list = []

while True:
    try:
        item = input("").capitalize()
        if item:
            if item in name_list:
                print("the name is already on there")
                continue
            else:
                name_list.append(item)

    except EOFError:
        if len(name_list) > 2:
            print("Adieu, adieu, to", ", ".join(name_list[:-1]) + ", and " + name_list[-1])
        elif len(name_list) > 1:
            print("Adieu, adieu, to", ", ".join(name_list[:-1]) + " and " + name_list[-1])
        else:
            print("Adieu, adieu, to", name_list[0])
        break
