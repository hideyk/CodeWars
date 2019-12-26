def solution(args):
    range_string = ''
    range_placeholder = []
    for i in range(0, len(args) - 1):
        if args[i] != args[i+1] - 1:
            if range_placeholder == []:
                range_string += str(args[i]) + ","
            else:
                range_placeholder.append(args[i])
                if len(range_placeholder) <= 2:
                    for x in range_placeholder:
                        range_string += str(x) + ","
                    range_placeholder.clear()
                else:
                    range_string += str(range_placeholder[0]) + "-" + str(range_placeholder[-1]) + ","
                    range_placeholder.clear()
            if i == len(args) - 2:
                range_string += str(args[i+1])
        else:
            range_placeholder.append(args[i])
            if i == len(args) - 2:
                if len(range_placeholder) == 1:
                    range_string += str(range_placeholder[0]) + "," + str(args[i+1])
                else:
                    range_string += str(range_placeholder[0]) + "-" + str(args[i+1])

    return range_string


def solution2(args):
    out = []
    beg = end = args[0]

    for n in args[1:] + [""]:
        if n != end + 1:
            if end == beg:
                out.append(str(beg))
            elif end == beg + 1:
                out.extend([str(beg), str(end)])
            else:
                out.append(str(beg) + "-" + str(end))
            beg = n
        end = n

    return ",".join(out)


range_interval = [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
result = solution(range_interval)
print(result)