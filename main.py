for index in range(4):
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_icon(IconNames.SMALL_DIAMOND)
    basic.pause(300)
    basic.clear_screen()
    basic.show_leds("""
        . . # . .
        . # # # .
        # # # # #
        . # # # .
        . . # . .
        """)
    basic.pause(300)
    basic.clear_screen()
    basic.show_leds("""
        # . # . #
        . # # # .
        # # # # #
        . # # # .
        # . # . #
        """)