#   Encode files into base 64 to put into contact.vcf
#   Encoder is used to encode profile pictures and pronunciations
import base64
import sys


def encode(file):
    with open(file, "rb") as target:
        encoded_string = base64.b64encode(target.read())
        return encoded_string.decode("utf-8")


def makeFile(file, encoded_string):
    with open(file, "w") as target:
        target.write(encoded_string)


if (len(sys.argv) != 2):
    print("Usage: python3 encode.py <file-path>")
    exit(1)

encoded_string = encode(sys.argv[1])
# -4 removes 3 letter file extension and 1 period
makeFile(sys.argv[1][:-4] + ".base64", encoded_string)
