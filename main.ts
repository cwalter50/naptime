input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Diamond)
    basic.showNumber(input.lightLevel())
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.EighthNote)
    basic.showNumber(input.soundLevel())
})
