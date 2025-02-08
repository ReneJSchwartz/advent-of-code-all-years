def day_01_part_1():
    # how many calories top elf carries in total?

    file = open("01input")  # 01example returns correct 24k calories
    contents = file.readlines()
    sums = [0]  # initial value for accessing 0 index
    elf_index = 0
    largest_number = 0

    for x in contents:
        if x != "\n":
            sums[elf_index] += int(x)
        else:
            sums.append(0)
            elf_index += 1

    for x in sums:
        if x > largest_number:
            largest_number = x

    return largest_number


def day_01_part_2():
    # how many calories top 3 elves carry in total?

    file = open("01input")  # 01example returns correct 24k calories
    contents = file.readlines()
    sums = [0]  # initial value for accessing 0 index
    elf_index = 0
    largest_number = 0

    for x in contents:
        if x != "\n":
            sums[elf_index] += int(x)
        else:
            sums.append(0)
            elf_index += 1

    sums.sort(reverse=True)

    total = sums[0] + sums[1] + sums[2]

    return total


if __name__ == '__main__':
    print(day_01_part_2())
