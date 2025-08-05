def main():
    time = input("What time is it? ").lower().strip()
    if "am" in time or "pm" in time:
        """time = am_pm(time)""" #This is how I would handle AM/PM. Granted, it only covers "am" and "pm", and not "A.M" and "P.M"; but it's the same principle, just a few more lines
    converted_time = convert(time)

    if 7 <= converted_time <= 8:
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("lunch time")
    elif 18 <= converted_time <= 19:
        print("dinner time")

def convert(time):
    hour, minute = time.split(":")
    hour = float(hour)
    minute = float(minute)
    return hour + (minute / 60)

"""def am_pm(time): #This is how I would handle AM/PM
    if "am" in time:
        time = time.strip("am")
        hour, minute = time.split(":")
        hour = int(hour)
        if hour == 12:
            hour = 00
            return str(hour) + f":{minute}"
        else:
            return str(hour) + f":{minute}"

    if "pm" in time:
        time = time.strip("pm")
        hour, minute = time.split(":")
        hour = int(hour) + 12
        if hour == 24:
            hour = 00
            return str(hour) + f":{minute}"
        else:
            return str(hour) + f":{minute}"
"""

if __name__ == '__main__':
    main()
