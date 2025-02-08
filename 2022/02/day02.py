from RPS import RPS


def day_2_part_1():
    lines = open("day02input").readlines()
    total = 0

    for rps_match in lines:
        opponent_shape = get_shape(rps_match[0])
        my_shape = get_shape(rps_match[2])
        total += my_shape.value
        total += match_points(opponent_shape, my_shape)

    return total


def day_2_part_2():
    lines = open("day02input").readlines()
    total = 0

    for rps_match in lines:
        opponent_shape = get_shape(rps_match[0])

        result = rps_match[2]
        if result == "X": # lose
            if opponent_shape == RPS.ROCK: my_shape = RPS.SCISSORS
            elif opponent_shape == RPS.PAPER: my_shape = RPS.ROCK
            elif opponent_shape == RPS.SCISSORS: my_shape = RPS.PAPER
        elif result == "Y": # draw
            if opponent_shape == RPS.ROCK: my_shape = RPS.ROCK
            elif opponent_shape == RPS.PAPER: my_shape = RPS.PAPER
            elif opponent_shape == RPS.SCISSORS: my_shape = RPS.SCISSORS
        elif result == "Z":  # win
            if opponent_shape == RPS.ROCK: my_shape = RPS.PAPER
            elif opponent_shape == RPS.PAPER: my_shape = RPS.SCISSORS
            elif opponent_shape == RPS.SCISSORS: my_shape = RPS.ROCK

        total += my_shape.value
        total += match_points(opponent_shape, my_shape)

    return total


def match_points(opponent_shape, my_shape):
    win = 6
    lose = 0
    tie = 3

    if my_shape == RPS.ROCK:
        if opponent_shape == RPS.ROCK: return tie
        if opponent_shape == RPS.PAPER: return lose
        if opponent_shape == RPS.SCISSORS: return win
    if my_shape == RPS.PAPER:
        if opponent_shape == RPS.ROCK: return win
        if opponent_shape == RPS.PAPER: return tie
        if opponent_shape == RPS.SCISSORS: return lose
    if my_shape == RPS.SCISSORS:
        if opponent_shape == RPS.ROCK: return lose
        if opponent_shape == RPS.SCISSORS: return tie
        if opponent_shape == RPS.PAPER: return win


def get_shape(symbol):
    if symbol == "X" or symbol == "A":
        return RPS.ROCK
    if symbol == "Y" or symbol == "B":
        return RPS.PAPER
    if symbol == "Z" or symbol == "C":
        return RPS.SCISSORS


if __name__ == '__main__':
    print(day_2_part_1())
