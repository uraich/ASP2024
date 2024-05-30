#**************************************************************************
#  This is an example for our Monochrome OLEDs based on SSD1306 drivers
#
#  Pick one up today in the adafruit shop!
#  ------> http://www.adafruit.com/category/63_98
#
#  This example is for a 128x64 pixel display using I2C to communicate
#  3 pins are required to interface (two I2C and one reset).

#  Adafruit invests time and resources providing this open
#  source code, please support Adafruit and open-source
#  hardware by purchasing products from Adafruit!

#  Written by Limor Fried/Ladyada for Adafruit Industries,
#  with contributions from the open source community.
#  BSD license, check license.txt for more information
#  All text above, and the splash screen below must be
#  included in any redistribution.
#  Ported from Arduino C++ version to MicroPython by U. Raich
#  for the African School of Physics 2024 
#  **************************************************************************

from micropython import const
from machine import Pin, I2C
from utime import sleep_ms
from random import random
import ssd1306,framebuf

SCREEN_WIDTH  = const(128)   # OLED display width, in pixels
SCREEN_HEIGHT = const(64)    # OLED display height, in pixels
SSD1306_BLACK = const(0)
SSD1306_WHITE = const(1)
NUMFLAKES     = const(10)    # Number of snowflakes in the animation example

LOGO_HEIGHT   = const(16)
LOGO_WIDTH    = const(16)

logo_bmp = bytearray([0b00000000, 0b11000000,
                      0b00000001, 0b11000000,
                      0b00000001, 0b11000000,
                      0b00000011, 0b11100000,
                      0b11110011, 0b11100000,
                      0b11111110, 0b11111000,
                      0b01111110, 0b11111111,
                      0b00110011, 0b10011111,
                      0b00011111, 0b11111100,
                      0b00001101, 0b01110000,
                      0b00011011, 0b10100000,
                      0b00111111, 0b11100000,
                      0b00111111, 0b11110000,
                      0b01111100, 0b11110000,
                      0b01110000, 0b01110000,
                      0b00000000, 0b00110000])

logo_mask = bytearray([0]*len(logo_bmp))
# invert all bits
for i in range(len(logo_mask)):
    logo_mask[i] = ~logo_bmp[i]

def clearDisplay():
    display.fill(SSD1306_BLACK)   

def testdrawline(): 

  clearDisplay()  # Clear display buffer

  for i in range(0, SCREEN_WIDTH,4) :
      display.line(0, 0, i, SCREEN_HEIGHT-1, SSD1306_WHITE);
      display.show() # Update screen with each newly-drawn line
      sleep_ms(1)
      
  for i in range(0, SCREEN_HEIGHT, 4):
      display.line(0, 0, SCREEN_WIDTH-1, i, SSD1306_WHITE)
      display.show()
      sleep_ms(1)
      
  sleep_ms(250)

  clearDisplay()

  for i in range(0, SCREEN_WIDTH, 4):
      display.line(0, SCREEN_HEIGHT-1, i, 0, SSD1306_WHITE)
      display.show()
      sleep_ms(1)
      
  for i in range(SCREEN_HEIGHT-1, 0, -4):
      display.line(0, SCREEN_HEIGHT-1, SCREEN_WIDTH-1, i, SSD1306_WHITE)
      display.show()
      sleep_ms(1)
      
  sleep_ms(250)
  
  clearDisplay();

  for i in range(SCREEN_WIDTH-1, 0, -4) :
      display.line(SCREEN_WIDTH-1, SCREEN_HEIGHT-1, i, 0, SSD1306_WHITE)
      display.show()
      sleep_ms(1)
      
  for i in range(SCREEN_HEIGHT-1, 0, -4) :
      display.line(SCREEN_WIDTH-1, SCREEN_HEIGHT-1, 0, i, SSD1306_WHITE)
      display.show()
      sleep_ms(1);
      
  sleep_ms(250)

  clearDisplay()

  for i in range(0, SCREEN_HEIGHT, 4):
      display.line(SCREEN_WIDTH-1, 0, 0, i, SSD1306_WHITE)
      display.show()
      sleep_ms(1)

  for i in range(0, SCREEN_WIDTH, 4):
      display.line(SCREEN_WIDTH-1, 0, i, SCREEN_HEIGHT-1, SSD1306_WHITE)
      display.show()
      sleep_ms(1)
      
  sleep_ms(2000) # Pause for 2 seconds

#------------------------------------------------------------------
def testdrawrect():
#------------------------------------------------------------------
    clearDisplay()

    for i in range(0, SCREEN_HEIGHT//2, 2):
        display.rect(i, i, SCREEN_WIDTH-2*i, SCREEN_HEIGHT-2*i, SSD1306_WHITE)
        display.show()  # Update screen with each newly-drawn rectangle
        sleep_ms(1)
        
    sleep_ms(2000)

#------------------------------------------------------------------
def testfillrect():
#------------------------------------------------------------------
    clearDisplay()
    drawing_color = SSD1306_WHITE
    for i in range(0, SCREEN_HEIGHT//2, 3):
        # The INVERSE color is used so rectangles alternate white/black
        display.fill_rect(i, i, SCREEN_WIDTH-i*2, SCREEN_HEIGHT-i*2, drawing_color)
        display.show() # Update screen with each newly-drawn rectangle
        if drawing_color == SSD1306_WHITE:
            drawing_color = SSD1306_BLACK           
        else:
            drawing_color = SSD1306_WHITE       
            sleep_ms(1);

    sleep_ms(2000);


def drawTriangle(p1_x,p1_y,p2_x,p2_y,p3_x,p3_y,color):
    display.line(p1_x,p1_y,p2_x,p2_y,color)
    display.line(p2_x,p2_y,p3_x,p3_y,color)
    display.line(p3_x,p3_y,p1_x,p1_y,color)
    
#------------------------------------------------------------------
def testdrawtriangle():
#------------------------------------------------------------------
    clearDisplay()

    for i in range(0, min(SCREEN_WIDTH,SCREEN_HEIGHT)//2, 5):
        drawTriangle(
            SCREEN_WIDTH//2  ,SCREEN_HEIGHT//2-i,
            SCREEN_WIDTH//2-i,SCREEN_HEIGHT//2+i,
            SCREEN_WIDTH//2+i,SCREEN_HEIGHT//2+i, SSD1306_WHITE)
        display.show()
        sleep_ms(1)

    sleep_ms(2000)

def min_3(x1,x2,x3): # calculate minimum or 3 values
    if x1 < x2:
        min_x = x1
    else :
        min_x = x2

    if min_x < x3:
        return min_x
    else :
        return x3
    
def max_3(x1,x2,x3): # calculate maximum or 3 values
    if x1 > x2:
        max_x = x1
    else :
        max_x = x2

    if max_x > x3:
        return max_x
    else :
        return x3
    
def drawFilledTriangle(p1_x,p1_y,p2_x,p2_y,p3_x,p3_y,color):
    # algorithm from
    # https://web.archive.org/web/20050408192410/http://sw-shader.sourceforge.net/rasterizer.html
    
    # Bounding rectangle

    minx = min_3(p1_x, p2_x, p3_x)
    maxx = max_3(p1_x, p2_x, p3_x)
    miny = min_3(p1_y, p2_y, p3_y)
    maxy = max_3(p1_y, p2_y, p3_y)

    # Scan through bounding rectangle
    for y in range(miny, maxy):
        for x in range(minx,maxx):
            # When all half-space functions are positive, pixel is in triangle
            if((p1_x - p2_x) * (y - p1_y) - (p1_y - p2_y) * (x - p1_x) > 0 and
               (p2_x - p3_x) * (y - p2_y) - (p2_y - p3_y) * (x - p2_x) > 0 and
               (p3_x - p1_x) * (y - p3_y) - (p3_y - p1_y) * (x - p3_x) > 0) :
                display.pixel(x, y, color)

#------------------------------------------------------------------
def testdrawfilledtriangle():
#------------------------------------------------------------------
    clearDisplay()
    color = SSD1306_BLACK
    # for i in range(0, min(SCREEN_WIDTH,SCREEN_HEIGHT)//2, 5):
    for i in range(min(SCREEN_WIDTH,SCREEN_HEIGHT)//2, -1, -5):
        # alternate colors
        if color == SSD1306_BLACK:
            color = SSD1306_WHITE
        else:
            color = SSD1306_BLACK
            
        # print("Color:", color)
        drawFilledTriangle(
            SCREEN_WIDTH//2  ,SCREEN_HEIGHT//2-i,
            SCREEN_WIDTH//2-i,SCREEN_HEIGHT//2+i,
            SCREEN_WIDTH//2+i,SCREEN_HEIGHT//2+i, color)
        display.show()
        sleep_ms(100)

    sleep_ms(2000)

#------------------------------------------------------------------
def testdrawcircle():
#------------------------------------------------------------------
    clearDisplay();

    for i in range(1, min(SCREEN_WIDTH,SCREEN_HEIGHT//2),5):
        # print(i)
        display.ellipse(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, i, i, SSD1306_WHITE)
        display.show()
        sleep_ms(1)

    sleep_ms(2000)

#------------------------------------------------------------------
def testdrawchar():
#------------------------------------------------------------------
    clearDisplay()

    # start with the blank character
    line = bytearray(16)
    for line_no in range(5):
        for i in range(16):
            line[i] = ord(' ') + 16*line_no + i
            text = line.decode()
        print(text)      
        display.text(text, 0, line_no*11,  SSD1306_WHITE)
          
    line_no +=1
    # all the characters except del    
    for i in range(15):
        line[i] = 0x20 + 16*line_no + i
        line[15] = ord(' ')
        text = line.decode()
    print(text)      
    display.text(text, 0, line_no*11,  SSD1306_WHITE)

    display.show()
    sleep_ms(2000)

def eraseBitmap(x_pos,y_pos,bitmap,bm_width,bm_height):
    fbuf = framebuf.FrameBuffer(logo_mask,
                                bm_width,bm_height,framebuf.MONO_HLSB)
    display.blit(fbuf, x_pos, y_pos, 1)
    display.show()
                                
def drawBitmap(x_pos,y_pos,bitmap,bm_width,bm_height):
    fbuf = framebuf.FrameBuffer(logo_bmp,
                                bm_width,bm_height,framebuf.MONO_HLSB)
    # for i in range(bm_height):
    #    print("{:02x} {:02x}".format(logo_bmp[2*i],
    #    logo_bmp[2*i+1]))
        
    display.blit(fbuf, x_pos, y_pos, 0)
    display.show()
    
#------------------------------------------------------------------
def testdrawbitmap():
#------------------------------------------------------------------
    clearDisplay()
    
    drawBitmap(
    (SCREEN_WIDTH  - LOGO_WIDTH ) // 2,
    (SCREEN_HEIGHT - LOGO_HEIGHT) // 2,    
    logo_bmp, LOGO_WIDTH, LOGO_HEIGHT)

    display.show()
    sleep_ms(2000);

    
#------------------------------------------------------------------
def testanimate(bitmap, w, h):
#------------------------------------------------------------------

    current_ypos = [0]*NUMFLAKES
    icons = [0,0,0]*NUMFLAKES
    XPOS   = 0 # Indexes into the 'icons' array in function below
    YPOS   = 1
    DELTAY = 2
    clearDisplay()  
    # Initialize 'snowflake' positions
    for f in range(NUMFLAKES):
        icons[f] = [int(random()*(SCREEN_WIDTH-LOGO_WIDTH)),
                          0,
                          int(random()*6) + 1]
        current_ypos[f] = 0   

    while True:
        # Draw each snowflake:
        for f in range(NUMFLAKES):
            # print("{:d}: x: {:d}, y: {:d}".format(
            #     f,icons[f][XPOS],icons[f][YPOS]))
            
            # erase the old flake and draw it again at the new position
            eraseBitmap(icons[f][XPOS], current_ypos[f], bitmap,
                        LOGO_WIDTH, LOGO_HEIGHT)
            # display.fill_rect(icons[f][XPOS],current_ypos[f],LOGO_WIDTH,LOGO_HEIGHT,
            #                   SSD1306_BLACK)
            current_ypos[f] = icons[f][YPOS]
            drawBitmap(icons[f][XPOS], icons[f][YPOS], bitmap,
                      LOGO_WIDTH, LOGO_HEIGHT)
    

            display.show()     # Show the display buffer on the screen

        sleep_ms(5)      # Pause for 5ms second
        # clear all the snowflakes and draw them at the new position
        #
        # Then update coordinates of each flake...
        for f in range(NUMFLAKES):
          icons[f][YPOS] += icons[f][DELTAY]
 
          # If snowflake is off the bottom of the screen...
          if icons[f][YPOS] >= SCREEN_HEIGHT:
              # clear the old snow flake
              display.fill_rect(icons[f][XPOS],current_ypos[f],LOGO_WIDTH,LOGO_HEIGHT,
                              SSD1306_BLACK)
              display.show()
              # Reinitialize to a random position, just off the top
              icons[f] = [int(random()*(SCREEN_WIDTH-LOGO_WIDTH)),
                          0,
                          int(random()*6) + 1]
              current_ypos[f] = 0  

# using default address 0x3C
i2c = I2C(1,sda=Pin(21), scl=Pin(22))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

print("Show current content of frame buffer")
display.show()
sleep_ms(2000)  # Pause for 2 seconds

# clear the buffer
clearDisplay()

# Draw a single pixel in white
print("Show a single pixel")
display.pixel(10, 10, SSD1306_WHITE)

# Show the display buffer on the screen. You MUST call display() after
# drawing commands to make them visible on screen!
display.show()
sleep_ms(2000)

# display.show() is NOT necessary after every single drawing command,
# unless that's what you want...rather, you can batch up a bunch of
# drawing operations and then update the screen all at once by calling
# display.show(). These examples demonstrate both approaches...

print("Line drawing")
testdrawline()      # Draw many lines
print("Drawing rectangles (outline)")
testdrawrect()      # Draw rectangles (outlines)
print("Drawing filled rectangles")
testfillrect()
print("Drawing triangles")
testdrawtriangle()        
print("Drawing filledtriangles")
testdrawfilledtriangle()       
print("Draw circles")
testdrawcircle()
print("Text drawing")
testdrawchar()
print("Drawing a logo")
testdrawbitmap()
# drawBitmap(
# (SCREEN_WIDTH  - LOGO_WIDTH ) // 2,
# 0,    
# logo_bmp, LOGO_WIDTH, LOGO_HEIGHT)
# sleep_ms(2000)
display.fill_rect((SCREEN_WIDTH  - LOGO_WIDTH ) // 2,0, LOGO_WIDTH, LOGO_HEIGHT ,0)
display.show()                  
print("test animate")
testanimate(logo_bmp,LOGO_WIDTH,LOGO_HEIGHT)

