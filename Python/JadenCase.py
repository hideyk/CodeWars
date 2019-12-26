def toJadenCase(words):
    string_list = words.split(" ")
    jadenWords = ""
    for word in string_list:
        jadenWords += word.capitalize()
        jadenWords += " "
    return jadenWords[:-1]


def toJadenCase2(string):
    return " ".join(w.capitalize() for w in string.split())

quote = "How can mirrors be real if our eyes aren't real"
jadenCase = toJadenCase(quote)
print(jadenCase)