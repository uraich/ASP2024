from machine import I2C,Pin
from micropython import const
SCL = const(22)
SDA = const(21)
BUS = const(1)

i2c = I2C(BUS, scl=Pin(SCL), sda=Pin(SDA)) # create a hardware I2C object on bus 1
slaves = i2c.scan()                        # scans the I2C bus and returns a list of
                                           # addresses of all connected I2C slaves

print("I2C slaves found:")                                           
for i in range(len(slaves)):
    print("0x{:02x} ".format(slaves[i]), end="");
print("")
    
