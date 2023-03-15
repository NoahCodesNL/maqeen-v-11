def on_button_pressed_a():
    for index in range(40):
        basic.show_leds("""
            . # . # .
                        # # # # #
                        # # # # #
                        . # # # .
                        . . # . .
        """)
        basic.show_icon(IconNames.SMALL_HEART)
input.on_button_pressed(Button.A, on_button_pressed_a)

basic.show_icon(IconNames.SQUARE)

def on_forever():
    pass
basic.forever(on_forever)
