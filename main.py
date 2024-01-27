radio.set_group(1)

def on_button_pressed_a():
    radio.send_string("Szia!")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(ReceivedString):
    basic.show_string(ReceivedString)
radio.on_received_string(on_received_string)

radio.set_group(1)

def on_button_pressed_b():
    radio.send_string("Hogy vagy?")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_string2(ReceivedString2):
    basic.show_string(ReceivedString2)
radio.on_received_string(on_received_string2)
