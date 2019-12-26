import math

def rectangle_rotation(a, b):
    aHalfBisect = (a/math.sqrt(2))/2
    bHalfBisect = (b/math.sqrt(2))/2
    rect1 = [math.floor(aHalfBisect) * 2 + 1, math.floor(bHalfBisect) * 2 + 1]
    rect2 = [0, 0]

    if aHalfBisect - math.floor(aHalfBisect) < 0.5:
        rect2[0] = rect1[0] - 1
    else:
        rect2[0] = rect1[0] + 1

    if bHalfBisect - math.floor(bHalfBisect) < 0.5:
        rect2[1] = rect1[1] - 1
    else:
        rect2[1] = rect1[1] + 1
    points = rect1[0] * rect1[1] + rect2[0] * rect2[1]
    return points


def rectangle_rotation2(a, b):
    a1 = filter(lambda x:x%2==0, [ a//(2**0.5), a//(2**0.5)+1 ])[0]
    a2 = filter(lambda x:x%2==1, [ a//(2**0.5), a//(2**0.5)+1 ])[0]
    b1 = filter(lambda x:x%2==0, [ b//(2**0.5), b//(2**0.5)+1 ])[0]
    b2 = filter(lambda x:x%2==1, [ b//(2**0.5), b//(2**0.5)+1 ])[0]
    return a1 * b1 + a2 * b2


length = 20
height = 16
no_points = rectangle_rotation(length, height)
print(no_points)