from collections import Counter
def scramble(s1, s2):
    c1, c2 = Counter(list(s1)), Counter(list(s2))
    for k, n in c2.items():
        if n > c1[k]:
            return False
    return True


def scrambleSlow(s1, s2):
    s1_list = list(s1)
    s2_list = list(s2)
    s1_len = len(s1_list)
    s2_len = len(s2_list)
    for i in s2_list:
        if i in s1_list:
            s1_list.remove(i)
        if len(s1_list) == s1_len - s2_len:
            return True
    return False


def scrambleBest(s1,s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True


def scrambleClever(s1,s2):
    # Counter basically creates a dictionary of counts and letters
    # Using set subtraction, we know that if anything is left over,
    # something exists in s2 that doesn't exist in s1
    return len(Counter(s2)- Counter(s1)) == 0


str1 = "steka"
str2 = "steakaa"
is_match = scramble(str1, str2)
print(is_match)