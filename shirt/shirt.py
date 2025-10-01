import sys, os
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        raise sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        raise sys.exit("Too many command-line arguments")

    in_file = sys.argv[1]
    out_file = sys.argv[2]

    if not os.path.exists(in_file):
        raise sys.exit(f"Could not read {in_file}")
    elif not in_file.endswith("jpg") and not in_file.endswith("png"):
        raise sys.exit("Invalid input")
    elif not out_file.endswith(in_file[-4:]):
        sys.exit("Input and output have different extensions")

    user_image = Image.open(in_file)
    cs50_shirt = Image.open("shirt.png")
    user_image = ImageOps.fit(user_image, cs50_shirt.size) #resize it to fit the shirt image size///by default it crops at the center
    user_image.paste(cs50_shirt, (0, 0), mask=cs50_shirt) #if it's mask, then transparent parts of the image are uzilized.. otherwise it just sits atop of the first image
    user_image.save(out_file) #I would also perhaps -- just in case -- add string to the saved file, so the user does not (accidentally) overwrite existing file(s), eg. user_image.save(f"new_{out_file}")


main()
