extends Node

@export var button_grid : Control

func _ready() -> void:
	for b : Button in button_grid.get_children():
		b.pressed.connect(open_level.bind(b))
	pass

func hide_menu():
	print("hide menu")
	pass

func open_level(sender):
	hide_menu()
	# todo open level
	print(sender.name)
	pass
