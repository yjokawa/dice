number = 0

def on_gesture_shake():
    global number
    number = randint(1, 6)
    basic.clear_screen()
    basic.show_number(number)
    if number == 1:
        basic.show_leds("""
            . . . . .
                        . . # . .
                        . # # # .
                        . . # . .
                        . . . . .
        """)
    elif number == 2:
        basic.show_leds("""
            # # . . .
                        # # . . .
                        . . . . .
                        . . . # #
                        . . . # #
        """)
    elif number == 3:
        basic.show_leds("""
            # . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . #
        """)
    elif number == 4:
        basic.show_leds("""
            # . . # #
                        # . . . .
                        . . . . .
                        . . . . #
                        # # . . #
        """)
    elif number == 5:
        basic.show_leds("""
            # . . . #
                        . . . . .
                        . . # . .
                        . . . . .
                        # . . . #
        """)
    else:
        basic.show_leds("""
            # # . # #
                        . . . . .
                        # # . # #
                        . . . . .
                        # # . # #
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
