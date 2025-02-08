lines = open("day04input").readlines()


def p1():
    a_greater = 0
    b_greater = 0
    start = 0
    end = 1

    for i in range(0, len(lines)):
        lines[i].rstrip()

    for x in range(0, len(lines)):
        sides = lines[x].split(',')
        a = sides[start].split('-')
        b = sides[end].rstrip().split('-')

        for y in range(0, 2):
            a[y] = int(a[y])
        for z in range(0, 2):
            b[z] = int(b[z])

        # subset
        if a[start] >= b[start] and a[end] <= b[end]:
            a_greater += 1
        elif b[start] >= a[start] and b[end] <= a[end]:
            b_greater += 1

    total = a_greater + b_greater
    print(a_greater, b_greater, total)


def p2():
    debug1 = 0
    debug2 = 0
    debug4 = 0
    debug3 = 0
    start = 0
    end = 1

    for i in range(0, len(lines)):
        lines[i].rstrip()

    for x in range(0, len(lines)):
        sides = lines[x].split(',')
        a = sides[start].split('-')
        b = sides[end].rstrip().split('-')

        for y in range(0, 2):
            a[y] = int(a[y])
        for z in range(0, 2):
            b[z] = int(b[z])

        if a[start] <= b[start] <= a[end]:
            debug1 += 1
        elif a[start] <= b[end] <= a[end]:
            debug2 += 1
        elif b[start] <= a[start] <= b[end]:
            debug3 += 1
        elif b[start] <= a[end] <= b[end]:
            debug4 += 1

    total = debug1 + debug2 + debug3 + debug4
    print(debug1, debug2, debug3, debug4, total)


if __name__ == '__main__':
    p2()
