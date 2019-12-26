def duplicate_count(text):
    return len([x for x in set(text.lower()) if text.lower().count(x) > 1])


jibberish = "aA"
duplicates = duplicate_count(jibberish)
print(duplicates)