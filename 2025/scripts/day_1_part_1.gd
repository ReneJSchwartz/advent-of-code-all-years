extends Node

@export var combination_lock : Sprite2D
var spin_time_per_degree = 0.01
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
	await get_tree().create_tween().tween_property(combination_lock, "rotation_degrees", combination_lock.rotation_degrees + 3.6 * 50, spin_time_per_degree * 50).finished
	print(combination_lock.rotation_degrees / 3.6)
	var count_of_zeroes = 0
	# now to do other rotations after initial starting point at 50
	for instruction in example_rotations.split("\n"):
		var dir = 1
		if instruction[0] == 'L':
			dir = -1
		var amt = int(instruction.substr(1))
		await get_tree().create_tween().tween_property(combination_lock, "rotation_degrees", combination_lock.rotation_degrees + 3.6 * amt * dir, spin_time_per_degree * amt).finished
		print(combination_lock.rotation_degrees / 3.6)
		if abs(combination_lock.rotation_degrees / 360) < 0.01:
			count_of_zeroes += 1
	
	print(count_of_zeroes)
