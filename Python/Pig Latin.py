def pig_it(text):
    return " ".join(i[1:] + i[0] + "ay" if i.isalpha() else i for i in text.split())


sentence = "Pig latin is cool !"
pigged = pig_it(sentence)
print(pigged)