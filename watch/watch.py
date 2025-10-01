import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if "src" in s and "iframe" in s:
        match = re.match(r'^(.*src=")?(https://|http://)?(www\.)?(youtube\.com)(/embed/)([0-9A-Za-z]*)(.*)?$', s)
        if match:
            return f"https://youtu.be/{match.group(6)}"
    return None

if __name__ == "__main__":
    main()
