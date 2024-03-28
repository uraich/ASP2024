from machine import Pin
from time import sleep_ms
USER_LED = 2
led = Pin(USER_LED,Pin.OUT)

led.on()
sleep_ms(500)
led.off()
