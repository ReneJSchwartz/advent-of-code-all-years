def p1():
    s1 = open("day06input").read()

    # s1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    c1 = ""
    c2 = ""
    c3 = ""
    c4 = ""

    for i in range(3, len(s1)):
        c1 = s1[i - 3]
        c2 = s1[i - 2]
        c3 = s1[i - 1]
        c4 = s1[i - 0]
        x = ''.join(set(c1 + c2 + c3 + c4))
        if len(x) == 4:
            print(x + " " + str(i + 1))
            break


def p2():
    s1 = open("day06input").read()

    # s1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    c1 = ""
    c2 = ""
    c3 = ""
    c4 = ""

    for i in range(3, len(s1)):
        c0 = s1[i - 0]
        c1 = s1[i - 1]
        c2 = s1[i - 2]
        c3 = s1[i - 3]
        c4 = s1[i - 4]
        c5 = s1[i - 5]
        c6 = s1[i - 6]
        c7 = s1[i - 7]
        c8 = s1[i - 8]
        c9 = s1[i - 9]
        c10 = s1[i - 10]
        c11 = s1[i - 11]
        c12 = s1[i - 12]
        c13 = s1[i - 13]

        x = ''.join(set(c0 + c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 + c10 + c11 + c12 + c13))
        if len(x) == 14:
            print(x + " " + str(i + 1))
            break


if __name__ == '__main__':
    p1()
    p2()
    
