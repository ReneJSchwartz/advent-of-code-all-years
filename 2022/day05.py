import re

lines = open("day05input").readlines()
cmds = []
move_amount = 0
from_stack = 1
to_stack = 2

# w1 = "ZN"  # example
# w2 = "MCD"  # example
# w3 = "P"  # example
w1 = "QFMRLWCV"
w2 = "DQL"
w3 = "PSRGWCNB"
w4 = "LCDHBQG"
w5 = "VGLFZS"
w6 = "DGNP"
w7 = "DZPVFCW"
w8 = "CPDMS"
w9 = "ZNWTVMPC"

# example
#     [D]
# [N] [C]
# [Z] [M] [P]
# input
# [V]     [B]                     [C]
# [C]     [N] [G]         [W]     [P]
# [W]     [C] [Q] [S]     [C]     [M]
# [L]     [W] [B] [Z]     [F] [S] [V]
# [R]     [G] [H] [F] [P] [V] [M] [T]
# [M] [L] [R] [D] [L] [N] [P] [D] [W]
# [F] [Q] [S] [C] [G] [G] [Z] [P] [N]
# [Q] [D] [P] [L] [V] [D] [D] [C] [Z]
#  1   2   3   4   5   6   7   8   9


def p1():
    cmd_index = 0
    for x in lines:
        x = re.findall(r'[0-9]+', x)
        cmd_l = [int(x[0]), int(x[1]), int(x[2])]
        cmds.append(cmd_l)
        move_boxes_one_by_one(cmds[cmd_index])
        cmd_index += 1

    print_all()
    print()


def move_boxes_one_by_one(instructions):
    start = instructions[from_stack]
    end = instructions[to_stack]
    amt = instructions[move_amount]

    from_word = get_word(start)
    rev = from_word[::-1]
    extraction = rev[:amt]
    to_word = get_word(end)

    new_from = from_word[:-amt]
    put_word(start, new_from)

    new_to = to_word.join(["", extraction])  # works at least, refactor target
    put_word(end, new_to)


def print_all_example(): print("1" + w1, "2" + w2, "3" + w3, sep=' ', end='')


def print_all():
    print(str(1)+w1, str(2)+w2, str(3)+w3, str(4)+w4, str(5)+w5,
          str(6)+w6, str(7)+w7, str(8)+w8, str(9)+w9, sep=' ', end='')


def get_word(number):
    if number == 1: return w1
    if number == 2: return w2
    if number == 3: return w3
    if number == 4: return w4
    if number == 5: return w5
    if number == 6: return w6
    if number == 7: return w7
    if number == 8: return w8
    if number == 9: return w9
    pass


# could also be done with dictionary put this is Python 3.9 switch case
# refactor to two-liner
def put_word(number, word):
    if number == 1:
        globals()['w1'] = word
    if number == 2:
        globals()['w2'] = word
    if number == 3:
        globals()['w3'] = word
    if number == 4:
        globals()['w4'] = word
    if number == 5:
        globals()['w5'] = word
    if number == 6:
        globals()['w6'] = word
    if number == 7:
        globals()['w7'] = word
    if number == 8:
        globals()['w8'] = word
    if number == 9:
        globals()['w9'] = word


def p2():
    cmd_index = 0
    for x in lines:
        x = re.findall(r'[0-9]+', x)
        cmd_l = [int(x[0]), int(x[1]), int(x[2])]
        cmds.append(cmd_l)
        move_many_boxes_simultaneously(cmds[cmd_index])
        cmd_index += 1

    print_all()


def move_many_boxes_simultaneously(instructions):
    start = instructions[from_stack]
    end = instructions[to_stack]
    amt = instructions[move_amount]

    from_word = get_word(start)
    extraction = from_word[-amt:]
    to_word = get_word(end)
    new_from = from_word[:-amt]
    put_word(start, new_from)

    new_to = to_word.join(["", extraction])  # works at least, refactor target
    put_word(end, new_to)


if __name__ == '__main__':
    p1() # VWLCWGSDQ

    # reset variables
    w1 = "QFMRLWCV"
    w2 = "DQL"
    w3 = "PSRGWCNB"
    w4 = "LCDHBQG"
    w5 = "VGLFZS"
    w6 = "DGNP"
    w7 = "DZPVFCW"
    w8 = "CPDMS"
    w9 = "ZNWTVMPC"

    p2()  # TCGLQSLPW
