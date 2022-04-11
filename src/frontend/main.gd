extends Node2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var heaters = []
var heaters_path = []

onready var heater_obj = load("res://src/scenes/HeaterPanel.tscn")

func from_txt():
	var f = File.new()
	f.open("data.txt", File.READ)
	var j_list = parse_json(f.get_line())
	f.close()
	return j_list
	
func generate_panels():
	for i in range(len(heaters)):
		var inst = heater_obj.instance()
		inst.rect_position = Vector2(96, 1000)
		print(heaters[i]["name"])
		inst.heater_name = heaters[i]["name"]
		inst.temp = str(heaters[i]["temp"]) + "°C"
		inst.hum = str(heaters[i]["hum"]) + "%"
		inst.togg = heaters[i]["state"]
		inst.index = i
		add_child(inst)
		heaters_path.append(inst.get_path())
		
func update():
	for i in range(len(heaters_path)):
		var obj = get_node(heaters_path[i])
		
		obj.heater_name = heaters[i]["name"]
		obj.temp = str(heaters[i]["temp"]) + "°C"
		obj.hum = str(heaters[i]["hum"]) + "%"
		obj.togg = heaters[i]["state"]
		obj.index = i

func _ready():
	heaters = from_txt()
	print(heaters)
	print(heater_obj)
	generate_panels()

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
	


func _on_Timer_timeout():
	heaters = from_txt()
	update()
	print("UPDATE!")
