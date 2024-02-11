# Pulse Rifle Ammo Counter/Sounds
# Feather TFT REV

# R. Wolfgang Rumpf 2/2024

# Designed for ESP32-S2 Feather with 240x135 TFT display
# needs .bcf or .pcf fonts

# Initialize python libraries #########################################

import time
import board
import displayio
import terminalio
import digitalio
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label
display = board.DISPLAY

# Initialize display ##################################################
display = board.DISPLAY
splash = displayio.Group()
display.show(splash)

# Initialize Fonts & Colors ###########################################
font1 = bitmap_font.load_font("/fonts/weyland10.bdf")
font2 = bitmap_font.load_font("/fonts/weyland12.bdf")
font3 = bitmap_font.load_font("/fonts/weyland14.bdf")
font4 = bitmap_font.load_font("/fonts/weyland36.bdf")
font5 = bitmap_font.load_font("/fonts/weyland72.bdf")
font6 = bitmap_font.load_font("/fonts/weyland108.bdf")

red = 0xff2a04
green = 0x199781
yellow = 0xe6ff05
blue = 0x0000FF

## Create text labels #################################################
header_label = label.Label(font2, text="Weyland-Yutani", color=red)
header_label.x = int(display.width / 2 - header_label.width / 2)
header_label.y = 10
splash.append(header_label)

subheader1_label = label.Label(font1, text="a subsidiary of", color=blue)
subheader_label1.x = int(display.width / 2 - subheader_label1.width / 2)
subheader_label1.y = 30
splash.append(subheader_label1)

subheader2_label = label.Label(font2, text="Stark Industries", color=blue)
subheader_label2.x = int(display.width / 2 - subheader_label2.width / 2)
subheader_label2.y = 50
splash.append(subheader_label2)

result_label = label.Label(font5, text="99", color=yellow)
result_label.x = 30
result_label.y = 75
splash.append(result_label)

# Initialize Buttons ###################################################

# Initialize buttons
fire_btn = digitalio.DigitalInOut(board.D1)
fire_btn.direction = digitalio.Direction.INPUT
fire_btn.pull = digitalio.Pull.DOWN

reset_btn = digitalio.DigitalInOut(board.D2)
reset_btn.direction = digitalio.Direction.INPUT
reset_btn.pull = digitalio.Pull.DOWN

# Loop forever  ########################################################
while True:








    pass
