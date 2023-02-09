let number = 0
input.onGesture(Gesture.Shake, function () {
    number = randint(1, 6)
    basic.clearScreen()
    if (number == 1) {
        basic.showLeds(`
            . . . . .
            . . # . .
            . # # # .
            . . # . .
            . . . . .
            `)
    } else if (number == 2) {
        basic.showLeds(`
            # # . . .
            # # . . .
            . . . . .
            . . . # #
            . . . # #
            `)
    } else if (number == 3) {
        basic.showLeds(`
            # . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . #
            `)
    } else if (number == 4) {
        basic.showLeds(`
            # . . # #
            # . . . .
            . . . . .
            . . . . #
            # # . . #
            `)
    } else if (number == 5) {
        basic.showLeds(`
            # . . . #
            . . . . .
            . . # . .
            . . . . .
            # . . . #
            `)
    } else {
        basic.showLeds(`
            # # . # #
            . . . . .
            # # . # #
            . . . . .
            # # . # #
            `)
    }
})
