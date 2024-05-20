# Raspberry Pi UCB Switch
The [Raspberry Pi UCB](https://www.thingiverse.com/thing:6618915/) is a Universal Casing Version B for the Raspberry Pi 5 with or without SSD (Pimoroni NVMe BASE) and HAT. 

The Raspberry Pi UCB is the B version (Better Version) for the Raspberry Pi 5 with cooling and HAT. The case can be used as a mini HTPC, NAS, SERVER and much more. The interchangeable covers allow it to be adapted to many different Raspberry Pi 5 configurations. You can use the case with an OSOYOO 5" touch display or with one of the popular Raspberry Pi UC front covers.

![Raspberry Pi UCB](https://github.com/HKHH/UCB_SWITCH/blob/main/image/frontswitch.png)

In this tutorial I would like to show you how to use the two switches on the front. For me, the lower switch is used to switch on and off and the upper switch is used to switch from the display or reboot with a long press. But you can also trigger other actions when pressed.

## Lower switch (POWER ON / OFF)
The Raspberry Pi 5 has a switch on the board with which you can boot the computer and perform a shutdown. But many people don't know that you can easily do this with an external switch.
To do this, you must solder two cables with a button at the marked location. If you also want to remove the switch, it is helpful to solder a 2-pin connector strip (distance 2.54) and connect the appropriate plugs.

## Top switch (SWITCH BETWEEN DISPLAY AND HDMI, REBOOT)
The second switch is connected via the 40 PIN GPIO strip, similar to the Raspberry Pi 3 and 4. However, due to the hardware change in Raspberry Pi 5, you can no longer use the libraries for GPIO control as with the old models. [GPIO Zero](https://gpiozero.readthedocs.io/en/stable/installing.html) was used for control.
If the switch is held for more than 3 seconds then another command will be executed. My script then reboots.

It is assumed that you have connected the cables from the button to [PIN 33 (GPIO 13) and PIN 34 (GND)](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html). If you want to use a different GPIO PIN, you must adapt the topswitch.py script accordingly.

### Installation
Copy the two configurations for the display and the HDMI output into the directory where the config.txt file is located (/boot/firmware) assign the appropriate access rights:
```
sudo cp config.DSI config.HDMI /boot/firmware
cd /boot/firmware
sudo chgrp root config.DSI config.HDMI
sudo chown root config.DSI config.HDMI
sudo chmod 755 config.DSI config.HDMI
```
If necessary, you can adjust the configurations according to your needs.
To switch the output, press the switch to copy one of the configuration files to config.txt and overwrite the existing config.txt. It is therefore advisable to make a backup copy of the config.txt file beforehand.

Now let's install the scripts that do this:
```
sudo cp changedisplayoutput topswitch.py /usr/sbin
cd /usr/sbin
sudo chgrp root changedisplayoutput topswitch.py
sudo chown root changedisplayoutput topswitch.py
sudo chmod 755 changedisplayoutput topswitch.py
```

So that the script is started automatically when booting, we have to ask it in the rc.local:
```
cd /etc
sudo nano rc.local
```
Add the following before exit 0:
```
/usr/sbin/topswitch.py &
```
Save and close the editor with CTRL + O and finally CTRL + X



