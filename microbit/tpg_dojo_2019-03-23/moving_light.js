let item = 0
let colourNumber = 0
let Pixel: neopixel.Strip = null
let colour = 0
input.onButtonPressed(Button.A, function () {
    if (colourNumber < 3) {
        colourNumber += 1
    } else {
        colourNumber = 0
    }
    if (colourNumber == 0) {
        colour = neopixel.colors(NeoPixelColors.Orange)
    }
    if (colourNumber == 1) {
        colour = neopixel.colors(NeoPixelColors.Purple)
    }
    if (colourNumber == 2) {
        colour = neopixel.colors(NeoPixelColors.Blue)
    }
    if (colourNumber == 3) {
        colour = neopixel.colors(NeoPixelColors.Green)
    }
})
input.onGesture(Gesture.Shake, function () {
    if (colour == neopixel.colors(NeoPixelColors.Red)) {
        colour = neopixel.colors(NeoPixelColors.Yellow)
    } else {
        colour = neopixel.colors(NeoPixelColors.Red)
    }
})
colour = neopixel.colors(NeoPixelColors.Red)
Pixel = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB)
item = 0
colourNumber = 0
basic.forever(function () {
    Pixel.setPixelColor(item, colour)
    if (item < 24) {
        item += 1
        Pixel.show()
        Pixel.clear()
    } else if (item >= 24) {
        item = 0
    }
})
