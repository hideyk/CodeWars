import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return set(s.lower()) >= alphabet

def is_pangram2(s):
    return set(string.lowercase) <= set(s.lower())
        
text = "The quick brown fox jumps over the lazy dog"
text_is_pangram = is_pangram(text)
print(text_is_pangram)