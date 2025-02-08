f = open("day08example").readlines()
trees = []
visible_trees_counter = 0
visible_trees_list = []

for line in f:
    line = line.rstrip('\n')
    # num_list = list(map(int, line))
    num_list = [int(x) for x in line]
    trees.append(num_list)

columns = len(trees)
rows = len(trees[0])

for r in range(0, columns):
    visible_trees_list.append(list(rows * "-"))
    tallest_tree = -1
    for c in range(rows):
        if trees[r][c] > tallest_tree:
            tallest_tree = trees[r][c]
            if visible_trees_list[r][c] != "^":
                visible_trees_counter += 1
                visible_trees_list[r][c] = "^"
    tallest_tree = -1
    for c in reversed(range(rows)):
        if trees[r][c] > tallest_tree:
            tallest_tree = trees[r][c]
            if visible_trees_list[r][c] != "^":
                visible_trees_counter += 1
                visible_trees_list[r][c] = "^"

for r in range(rows):
    tallest_tree = -1
    for c in range(columns):
        if trees[c][r] > tallest_tree:
            tallest_tree = trees[c][r]
            if visible_trees_list[c][r] != "^":
                visible_trees_counter += 1
                visible_trees_list[c][r] = "^"
    tallest_tree = -1
    for c in reversed(range(columns)):
        if trees[c][r] > tallest_tree:
            tallest_tree = trees[c][r]
            if visible_trees_list[c][r] != "^":
                visible_trees_counter += 1
                visible_trees_list[c][r] = "^"


for line in trees:
    print(line)

for line in visible_trees_list:
    print()
    for contents in line:
        print(contents, end=' ')

print("\np1 visible trees: " + str(visible_trees_counter))

# p2
f = open("day08input").readlines()
trees = []
visible_trees_counter = 0
visible_trees_list = []

for line in f:
    line = line.rstrip('\n')
    # num_list = list(map(int, line))
    num_list = [int(x) for x in line]
    trees.append(num_list)

columns = len(trees)
rows = len(trees[0])
scenic_trees = []
highest_scenic_score = 0


# from top to bottom
for y in range(0, rows):
    if y == 0 or y == rows - 1:
        continue

    # from left to right
    for x in range(0, columns):

        height = trees[y][x]
        sees_trees_amt = 0
        viewing_distances = []

        # left trees
        for tree in reversed(range(0, x)):
            sees_trees_amt += 1
            if trees[y][tree] >= height:
                break

        #print("l trees for " + str(x) + ": " + str(sees_trees_amt))

        viewing_distances.append(sees_trees_amt)
        sees_trees_amt = 0

        # right trees
        for tree in range(x, columns - 1):
            sees_trees_amt += 1
            if trees[y][tree + 1] >= height:
                break

        viewing_distances.append(sees_trees_amt)

        #print("r trees for " + str(x) + ": " + str(sees_trees_amt))
        sees_trees_amt = 0

        # up trees
        for tree in reversed(range(0, y)):
            sees_trees_amt += 1
            if trees[tree][x] >= height:
                break

        #print("u trees for " + str(x) + ": " + str(sees_trees_amt))
        viewing_distances.append(sees_trees_amt)
        sees_trees_amt = 0

        # down trees
        for tree in range(y, rows - 1):
            sees_trees_amt += 1
            if trees[tree + 1][x] >= height:
                break

        #print("d trees for " + str(x) + ": " + str(sees_trees_amt))
        viewing_distances.append(sees_trees_amt)
        print(viewing_distances)


        # CALCULATES SCENIC SCORE
        scenic_score = 1
        for amt in viewing_distances:
            scenic_score *= amt
        #print(scenic_score)
        if scenic_score > highest_scenic_score:
            highest_scenic_score = scenic_score
        #print()

print("p2 highest scenic score tree was " + str(highest_scenic_score))
