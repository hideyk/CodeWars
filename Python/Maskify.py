def maskify(cc):
    length = len(cc) - 4
    unmasked = cc[-4:]
    masked = length * "#"
    return masked + unmasked

# return masked string
def maskify2(cc):
    return "#"*(len(cc)-4) + cc[-4:]


quote = "hello there"
masked = maskify(quote)
print(masked)
