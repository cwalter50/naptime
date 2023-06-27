def on_button_pressed_a():
    basic.show_icon(IconNames.DIAMOND)
    basic.show_number(input.light_level())
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_icon(IconNames.YES)
    basic.show_number(input.sound_level())
input.on_button_pressed(Button.B, on_button_pressed_b)
