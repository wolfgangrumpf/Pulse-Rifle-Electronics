# Write your code here :-)
# Pulse Rifle Ammo Counter/Sounds
# Feather TFT REV

# R. Wolfgang Rumpf 2/2024
# Dadsvacay short 2/17/204 minor update for classic movie font

# Designed for ESP32-S2 Feather with 240x135 TFT display
# needs .bcf or .pcf fonts

# Initialize python libraries #########################################

import board
import displayio
import digitalio
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
import time  # Import the time module for debounce
import audiocore
import audiobusio

# Initialize display ##################################################
display = board.DISPLAY
splash = displayio.Group()
display.show(splash)
display.auto_refresh = True

# Initialize audio ####################################################
audio = audiobusio.I2SOut(board.A0, board.A1, board.A2)
with open("prfire.wav", "rb") as wave_file:
    wav = audiocore.WaveFile(wave_file)

# Initialize variables ################################################
ammo = 95

# Initialize Fonts & Colors ###########################################
font2 = bitmap_font.load_font("/fonts/weyland12.bdf")
font3 = bitmap_font.load_font("/fonts/weyland14.bdf")
font5 = bitmap_font.load_font("/fonts/DSEG7Classic-Bold-99.bdf")

# Preload digits for faster rendering first-run
font5.load_glyphs(b"0123456789")

red = 0xFF2A04
green = 0x199781
yellow = 0xE6FF05
blue = 0x0000FF

# Create text labels #################################################


result_label = label.Label(font5, text=str(ammo), color=red)
result_label.x = 30
result_label.y = 75
splash.append(result_label)

# Initialize Buttons ###################################################

# Initialize buttons
fire_btn = digitalio.DigitalInOut(board.D5)  # Change to the desired pin, e.g., D5
fire_btn.direction = digitalio.Direction.INPUT
fire_btn.pull = digitalio.Pull.UP

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
                ammo = 95
                result_label.text = str(ammo)
                print("reset")
                audio.play(wav)
            last_reset_time = current_time

    # Fire button (no debounce)
    if not fire_btn.value:
        print("fire")
        print(ammo)
        ammo = max(0, ammo - 1)
        result_label.text = str(ammo)
        # play sound
        # audio.play(wav)

    display.refresh()

# TO DO

# sound:  https://learn.adafruit.com/esp32-s2-reverse-tft-feather/i2s
# find valid pulse rifle wav (create)
# clean up console reporting once debugged
