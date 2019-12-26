import string
import re


def alphabet_position(text):
    regex = re.compile('[^a-zA-Z]')
    text = regex.sub('', text)
    return "".join(str(string.ascii_lowercase.index(i.lower()) + 1) + " " for i in list(text))[:-1]


def alphabet_position2(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())


words = "The sunset sets at twelve o' clock."
replaced = alphabet_position(words)
print(replaced)