# Pulse-Rifle-Electronics

![pulsecounter](https://github.com/wolfgangrumpf/Pulse-Rifle-Electronics/assets/1257828/01b1da43-a1ab-49d7-adb1-a9d38032a215)

CircuitPython code for the Adafruit Feather TFT Reverse S2 to provide sound and lighting (ammo counter and firing sound) for a 3D printed Pulse Rifle.

Trigger button counts down ammo and plays a firing wav file.  When the counter reaches zero, NOTHING happens until you hit the RESET button.  This can
be integrated into the ammo clip if you like; by default reset is one of the front panel buttons currently.

Code is written so that you can use the front buttons or the GPIO pins to trigger both firing and resetting.  Wiring a switch to the trigger and another to the ammo
holder (perhaps a magnetic sensor switch) is easy enough.  If you have any thoughts or suggestions on additional functionality let me know.

If your Feather doesn't mount up like a flash drive you'll have to follow the instructions to switch the board to circuitpython mode.  Adafruit has all the info.

TO BE DONE:

I2C audio for WAV playback still needs to be implemented
