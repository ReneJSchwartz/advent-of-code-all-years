ascii_lower_offset = 96
ascii_upper_offset = 38
lines = open("day03input").readlines()


def p1():
    total = 0

    for x in lines:
        first_half = x[:int((len(x) - 1) * 0.5)]
        second_half = x[int((len(x) - 1) * 0.5):]

        for i in range(0, len(first_half)):
            letter = first_half[i]
            if second_half.__contains__(letter):
                total += ord(letter) - ascii_upper_offset if letter.isupper() else ord(letter) - ascii_lower_offset
                break
    print(total)


def p2():
    total = 0

    for i in range(0, len(lines), 3):
        for j in range(0, len(lines[i])):
            letter = lines[i][j]
            if lines[i + 1].__contains__(letter) and lines[i + 2].__contains__(letter):
                total += ord(letter) - ascii_upper_offset if letter.isupper() else ord(letter) - ascii_lower_offset
                break

    print(total)


if __name__ == '__main__':
    p1()
