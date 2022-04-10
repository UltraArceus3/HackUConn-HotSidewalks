extends Panel


export var toggle: bool = false


# Called when the node enters the scene tree for the first time.
func _ready():
	pass


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(_delta):
	if toggle:
		$LabelTogg.text = "ON"
		modulate = Color(0, 1, 0)
	else:
		$LabelTogg.text = "OFF"
		modulate = Color(1, 0, 0)
