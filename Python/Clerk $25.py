def tickets(people):
    curr_change = {25:0, 50:0, 100:0}
    for i in people:
        if i == 25:
            curr_change[25] += 1
        if i == 50:
            curr_change[25] -= 1
            curr_change[50] += 1
        if i == 100:
            if curr_change[50] > 0:
                curr_change[25] -= 1
                curr_change[50] -= 1
            else:
                curr_change[25] -= 3
            curr_change[100] += 1

        if curr_change[25] <= -1 or curr_change[50] <= -1:
            return "NO"
    return "YES"

people_array = [25, 50, 100]
cansell = tickets(people_array)
print(cansell)
