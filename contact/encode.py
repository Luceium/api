import base64


def encode(file):
    with open(file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data)

# Inserts the encoded data into the file and replaces the target string


def insertEncoding(file, data, target):
    with open(file, 'r+') as f:
        content = f.read()
        content = content.replace(target, str(data)[3:-1])
        f.seek(0)
        f.write(content)
        f.truncate()


data = encode('contact/profile.jpg')
insertEncoding('contact/contact.vcf', data, '%INSERT_PHOTO%')
data = encode('contact/pronunciation.ogg')
insertEncoding('contact/contact.vcf', data, '%INSERT_PRONUNCIATION%')
