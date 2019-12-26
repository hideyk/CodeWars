def solution(string,markers):
    string_array = string.split("\n")
    for i in range(len(string_array)):
        for j in markers:
            string_array[i] = string_array[i].split(j)[0]
            string_array[i] = string_array[i].rstrip()
    return "\n".join(i for i in string_array)


def solution2(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)

text = "apples, pears # and bananas\ngrapes\nbananas !apples"
marker = ["#", "!"]
result = solution(text, marker)
print(result)