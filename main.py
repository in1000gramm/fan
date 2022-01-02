def stop():
    pins.digital_write_pin(DigitalPin.P0, 0)
    pins.digital_write_pin(DigitalPin.P1, 0)

def on_button_pressed_a():
    start(100)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    stop()
input.on_button_pressed(Button.B, on_button_pressed_b)

def start(fan: number):
    pins.digital_write_pin(DigitalPin.P0, 0)
    pins.analog_write_pin(AnalogPin.P1, fan)
led.enable(True)