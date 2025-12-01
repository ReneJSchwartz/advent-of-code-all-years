class_name Day1
extends Node
## Combination lock is rotated left or right some amount and door password is 
## deducted from how many times the lock lands on 0 or passes it.
## Rotating a lock sprite takes a long ass time (1-20 min) and floating point 
## errors made me do this with just regular math, but I got pretty close with 
## rotation animations too.

var example_rotations : String = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

func _ready() -> void: 
	var count_of_zeroes = 0
	# Starting at 50 on the lock dial. This number is always between 0 and 99.
	var location = 50
	var part = 2
	
	# count how many times wheel lands on 0
	if part == 1:
		for instruction in example_rotations.split("\n"):
			var dir = 1 if instruction[0] == 'R' else -1
			var amt = int(instruction.substr(1))
			location += dir * amt
			if location % 100 == 0:
				count_of_zeroes += 1
		print(count_of_zeroes)
	
	# count how many times wheel clicks on 0
	if part == 2:
		for instruction in example_rotations.split("\n"):
			var dir = 1 if instruction[0] == 'R' else -1
			var amt = int(instruction.substr(1))
			for x in range(amt):
				location += dir
				if location == -1:
					location = 99
				elif location == 100:
					location = 0
				
				if location == 0:
					count_of_zeroes += 1
		print(count_of_zeroes)
