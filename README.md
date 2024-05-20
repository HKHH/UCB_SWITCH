# Raspberry Pi UCB Switch
The [Raspberry Pi UCB](https://www.thingiverse.com/thing:6618915/) is a Universal Casing Version B for the Raspberry Pi 5 with or without SSD (Pimoroni NVMe BASE) and HAT. 

The Raspberry Pi UCB is the B version (Better Version) for the Raspberry Pi 5 with cooling and HAT. The case can be used as a mini HTPC, NAS, SERVER and much more. The interchangeable covers allow it to be adapted to many different Raspberry Pi 5 configurations. You can use the case with an OSOYOO 5" touch display or with one of the popular Raspberry Pi UC front covers.

In this tutorial I would like to show you how to use the two switches on the front

## Lower switch (POWER ON / OFF)
The Raspberry Pi 5 has a switch on the board with which you can boot the computer and perform a shutdown. But many people don't know that you can easily do this with an external switch.
To do this, you must solder two cables with a button at the marked location. If you also want to remove the switch, it is helpful to solder a 2-pin connector strip (distance 2.54) and connect the appropriate plugs.

## Top switch (SWITCH BETWEEN DISPLAY AND HDMI, REBOOT)
The second switch is connected via the 40 PIN GPIO strip, similar to the Raspberry Pi 3 and 4. However, due to the hardware change in Raspberry Pi 5, you can no longer use the libraries for GPIO control as with the old models. [GPIO Zero](https://gpiozero.readthedocs.io/en/stable/installing.html) was used for control.

