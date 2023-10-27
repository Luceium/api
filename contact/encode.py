#   Encode files into base 64 to put into contact.vcf
#   Encoder is used to encode profile pictures and pronunciations
import base64
import sys


def encode(file):
    with open(file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        return encoded_string.decode("utf-8")


if (len(sys.argv) != 2):
    print("Usage: python3 encode.py <file-path>")
    exit(1)
