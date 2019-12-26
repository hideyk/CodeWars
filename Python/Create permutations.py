from itertools import permutations


def permutations(string):
    permList = permutations(string)
    permL = []
    for perm in list(permList):
        permL.append("".join(perm))
    return permL


text = "aab"
permutation_set = permutations(text)
print(permutation_set)