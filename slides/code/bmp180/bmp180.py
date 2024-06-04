#  Reads the BMP180 ID register
#

from machine import I2C,Pin
from micropython import const
from utime import sleep_ms
import sys

SCL = const(22)
SDA = const(21)
BUS = const(1)
BMP180_ADDR          = 0x77
BMP180_ID_REG        = 0xd0 # address of IF register
BMP180_CTRL_MEAS_REG = 0xf4
BMP180_MEAS_TEMP     = 0x2e

i2c = I2C(BUS, scl=Pin(SCL), sda=Pin(SDA))
# scan the I2C bus
i2c_addr = i2c.scan()
if BMP180_ADDR in i2c_addr:
    print("BMP180 address found")
else:
    print("No BMP180 found on the I2C bus, please check the cabling")
    sys.exit(-1)
    
id = i2c.readfrom_mem(BMP180_ADDR,BMP180_ID_REG,1)[0]
print("ID register read: 0x{:02x}".format(id))
# start a temperature measurement
i2c.writeto_mem(BMP180_ADDR, BMP180_CTRL_MEAS_REG, bytearray([BMP180_MEAS_TEMP]))
ctrl = i2c.readfrom_mem(BMP180_ADDR, BMP180_CTRL_MEAS_REG,1)[0]
print("ctrl register after temperature measurement request: 0x{:02x}".format(ctrl))
sleep_ms(10)
ctrl = i2c.readfrom_mem(BMP180_ADDR, BMP180_CTRL_MEAS_REG,1)[0]
print("ctrl register after some delay: 0x{:02x}".format(ctrl))
