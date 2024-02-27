# Pulse-Rifle-Electronics

![pulsecounter](https://github.com/wolfgangrumpf/Pulse-Rifle-Electronics/assets/1257828/01b1da43-a1ab-49d7-adb1-a9d38032a215)

This project contains the resources and CircuitPython code to add an ammo counter and firing sound to a 3D printed M41A Pulse Rifle.  This is designed for the Adafruit Feather TFT Reverse S2 and an I2S 3W Class D Amplifier Breakout MAX98357A (although you could probably make this work on any device that runs circuit python and modify the code for a different amp).

The wiring diagram below displays the general wiring for the Feather and the Amplifier. You'll want to use a pin for the trigger button (I used pin 5 in the code, so that's the easiest path) and connect a switch to that and ground, then make sure that switch is activated by your trigger.

Once booted up, the Trigger button counts down ammo and plays a firing wav file.  When the counter reaches zero, NOTHING happens until you hit the RESET button.  This can be integrated into the ammo clip if you like; by default reset is one of the front panel buttons currently.

While the code is written so that you can use the front buttons to trigger a reset, wiring a switch to the ammo insert (maybe a magnetic switch) would work too.  If you can think of any other functionality you'd like, let me know.

If your Feather doesn't mount up like a flash drive you'll have to follow the instructions to switch the board to circuitpython mode.  Adafruit has all the info.

![adafruit_products_FRTFT_I2S_bb](https://github.com/wolfgangrumpf/Pulse-Rifle-Electronics/assets/1257828/91be9ee3-fff1-4d7c-8115-7adc85acd0cd)

