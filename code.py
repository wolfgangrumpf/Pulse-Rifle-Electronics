# Pulse Rifle Ammo Counter/Sounds
# Feather TFT REV

# R. Wolfgang Rumpf 2/2024

# Designed for ESP32-S2 Feather with 240x135 TFT display
# needs .bcf or .pcf fonts

# Initialize python libraries #########################################

import board
import displayio
import digitalio
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
import time  # Import the time module for debounce
display = board.DISPLAY

# Initialize display ##################################################
display = board.DISPLAY
splash = displayio.Group()
display.show(splash)
display.auto_refresh = True

# Initialize variables ################################################
ammo = 99

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
header_label = label.Label(font3, text="Weyland-Yutani", color=red)
header_label.x = int(display.width / 2 - header_label.width / 2)
header_label.y = 10
splash.append(header_label)

subheader_label1 = label.Label(font2, text="A Stark Subsidiary", color=blue)
subheader_label1.x = int(display.width / 2 - subheader_label1.width / 2)
subheader_label1.y = 35
splash.append(subheader_label1)

result_label = label.Label(font5, text=str(ammo), color=yellow)
result_label.x = 30
result_label.y = 75
splash.append(result_label)

# Initialize Buttons ###################################################

# Initialize buttons
fire_btn = digitalio.DigitalInOut(board.D5)  # Change to the desired pin, e.g., D5
fire_btn.direction = digitalio.Direction.INPUT
fire_btn.pull = digitalio.Pull.DOWN

reset_btn = digitalio.DigitalInOut(board.D2)
reset_btn.direction = digitalio.Direction.INPUT
reset_btn.pull = digitalio.Pull.DOWN

# Define debounce delay in seconds
DEBOUNCE_DELAY = 0.1

# Initialize last reset button state variables
last_reset_state = False

# Initialize last reset button press time variables
last_reset_time = time.monotonic()

# Loop forever  ########################################################
while True:
    current_time = time.monotonic()

    # Debounce reset button
    if current_time - last_reset_time > DEBOUNCE_DELAY:
        current_reset_state = reset_btn.value
        if current_reset_state != last_reset_state:
            last_reset_state = current_reset_state
            if current_reset_state:
                ammo = 99
                result_label.text = str(ammo)
                print("reset")
            last_reset_time = current_time

    # Fire button (no debounce)
    if fire_btn.value:
        print("fire")
        print(ammo)
        ammo = max(0, ammo - 1)
        result_label.text = str(ammo)
        # play sound

    display.refresh()
