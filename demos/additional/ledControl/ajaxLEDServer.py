# ajaxMeasServer makes a measurement on the SHT30 when a, AJAX request comes
# in from the browser. It the constructs a message containing the measurement
# results and a timestamp. These data are then displayed in a table on the
# browser. The program needs the sensor.html file installed in the
# html directory of the ESP32
# Program written for the IoT course at the University of Cape Coast
# copyright (c) U. Raich June 2020
# This program is released under GPL

import picoweb
import time
import network
import uasyncio as asyncio
from machine import Pin

led=Pin(2,Pin.OUT) 
       
print ("Connecting to the network")
ap_if = network.WLAN(network.AP_IF)

if ap_if.active():
    print("Network interface is active")
else:
    print("Network interface is inactive, activating it...")
    ap_if.active(True)
    timeout=0
    for _ in range(100):   # timeout of 1s
        if ap_if.active():
            break;
        else:
            sleep_ms(10)
            timeout += 1
    if not ap_if.active():
        print("Problem activating the network interface")
        sys.exit()
    else:
        print("Network interface has been successfully activated")
ipaddr="192.168.4.1"
print("Starting a simple javascript WEB server")

app = picoweb.WebApp("__main__")

@app.route("/")
@app.route("/dummyLED")
def index(req, resp):
  print(req)
  yield from app.sendfile(resp,'html/dummyLED.html',content_type = "text/html")

@app.route("/ledControl")
def index(req, resp):
  print(req)
  yield from app.sendfile(resp,'html/ledControl.html',content_type = "text/html")
      
@app.route("/ledOn")
def index(req, resp):
  led.on() 
  print("led on")
  yield from picoweb.start_response(resp, content_type = "text/html")
  yield from resp.awrite("led=on")
  
@app.route("/ledOff")
def index(req, resp):
  led.off()   
  print("led off")
  yield from picoweb.start_response(resp, content_type = "text/html")
  yield from resp.awrite("led=off")
  
app.run(debug=2, host = ipaddr,port=80)
