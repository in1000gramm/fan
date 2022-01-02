function stop () {
    pins.digitalWritePin(DigitalPin.P0, 0)
    pins.digitalWritePin(DigitalPin.P1, 0)
}
input.onButtonPressed(Button.A, function () {
    basic.showString("It's fun")
    start(1000)
})
input.onButtonPressed(Button.B, function () {
    stop()
})
function start (fan: number) {
    pins.digitalWritePin(DigitalPin.P0, 0)
    pins.analogWritePin(AnalogPin.P1, fan)
}
