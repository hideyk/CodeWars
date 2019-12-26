def pascals_triangle(n):
    pascal_numbers = [1]
    if n == 1:
        return pascal_numbers

    for dep in range(1, n):
        pascal_numbers.append(1)
        temp = []
        for i in range(dep - 1):
            temp.append(pascal_numbers[-3 - i] + pascal_numbers[-2 - i])
        pascal_numbers += temp
        pascal_numbers.append(1)

    return pascal_numbers


# 2 -> [1, 1, 1]
# 3 -> [1, 1, 1, 1, 2, 1]
# 4 -> [1, 1, 1, 1, 2, 1, 1, 3, 3, 1]
# 5 -> [1, 1, 1, 1, 2, 1, 1, 3, 3, 1, 1, 4, 6, 4, 1]

depth = 6
pascals_list = pascals_triangle(depth)
print(pascals_list)