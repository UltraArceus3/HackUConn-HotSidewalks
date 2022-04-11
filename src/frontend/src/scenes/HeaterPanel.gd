extends Panel


var heater_name = ""
var temp = "temp"
var hum = "hum"
var togg = "OFF"

export var index = 0


# Called when the node enters the scene tree for the first time.
func _ready():
	pass


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	rect_position = rect_position.linear_interpolate(Vector2(128, (64*index) + 64), 0.1)
	
	$LabelName.text = heater_name
	$TempPanel/LabelTemp.text = temp
	$HumPanel/LabelHum.text = hum
	$ToggPanel.toggle = togg
