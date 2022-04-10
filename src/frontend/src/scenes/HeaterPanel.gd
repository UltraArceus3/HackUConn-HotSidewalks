extends Panel


onready var heater_name = $LabelName.text
onready var temp = $TempPanel/LabelTemp.text
onready var hum = $HumPanel/LabelHum.text
onready var togg = $ToggPanel/LabelTogg.text

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
