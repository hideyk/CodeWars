def in_array(array1, array2):
    returned_array = list(set([i for i in array1 if any(i in j for j in array2)]))
    returned_array.sort()
    return returned_array


def in_array2(a1, a2):
    return sorted({sub for sub in a1 if any(sub in s for s in a2)})


def in_array3(array1, array2):
    # your code
    res = []
    for a1 in array1:
        for a2 in array2:
            if a1 in a2 and not a1 in res:
                res.append(a1)
    res.sort()
    return res

a1 = ["tarp", "mice", "bull"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = in_array(a1, a2)
print(r)