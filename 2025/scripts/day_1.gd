extends Node

@export var combination_lock : Sprite2D
var spin_time_per_degree = 0.00005
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
	# starting location of 50 / 100
	var location = 50
	var part = 2
	
	# count how many times wheel lands on 0
	if part == 1:
		#await get_tree().create_tween().tween_property(combination_lock, "rotation_degrees", combination_lock.rotation_degrees + 3.6 * 50, spin_time_per_degree * 50).finished
		#print(combination_lock.rotation_degrees / 3.6)s
		# now to do other rotations after initial starting point at 50
		for instruction in example_rotations.split("\n"):
			var dir = 1
			if instruction[0] == 'L':
				dir = -1
			var amt = int(instruction.substr(1))
			location += dir * amt
			#await get_tree().create_tween().tween_property(combination_lock, "rotation_degrees", combination_lock.rotation_degrees + 3.6 * amt * dir, spin_time_per_degree * amt).finished
			if location % 100 == 0:
				count_of_zeroes += 1
		print(count_of_zeroes)
	
	# count how many times wheel clicks on 0
	if part == 2:
		for instruction in example_rotations.split("\n"):
			var dir = 1
			if instruction[0] == 'L':
				dir = -1
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
