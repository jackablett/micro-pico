import machine
import time

# https://github.com/jackablett/micro-pico/blob/main/documentation/modules/led.md

on_board_led = machine.Pin('LED', machine.Pin.OUT) # Defines the LED to a shorter variable

def toggle():
    on_board_led.toggle() # Uses the LED built in toggle function
    
def on():
    on_board_led.on() # Uses the LED built in on function
    
def off():
    on_board_led.off() # Uses the LED built in off function

def blink(ammount = int, duration = int): # Function takes ammount of flashes and the duration of each
    for i in range(ammount): # Repeats the script below the ammount of inputed value
        on() # Uses the defined functions above
        time.sleep(duration) # Sleep ammount of inputed time in seconds
        off()
        time.sleep(duration)
