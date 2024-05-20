#!/usr/bin/python3
# Script for the front top switch from the Raspberry Pi UCB

from gpiozero import Button
import subprocess, shlex, time, sys, syslog, os

######################################################################################
# System configuration
# The switch is connected to GND and PIN33 (GPIO13)
BUTTON = Button(13) #GPIO13 

# Operating system commando with all args that should be executed on short press
COMMAND_SHORTPRESS = "changedisplayoutput"

# Time for the longpress in seconds
TIME_LONGPRESS = float(3)

# Operating system commando with all args that should be executed on long press
COMMAND_LONGPRESS = "reboot"


# End system configuration
######################################################################################


# Check whether the script is being executed with the root user
uid = os.getuid()
if uid > 0:
  print ("The script needs root rights! Please execute the script with the root user.")
  sys.exit(0)

# Duration of the key press
PRESSURE_DURATION = float(0)

# Main

def start_timer():
    global PRESSURE_DURATION
    PRESSURE_DURATION = time.time()


def execute_command():
  if PRESSURE_DURATION > 0:
    measured_time = (time.time() - PRESSURE_DURATION)
    if measured_time > TIME_LONGPRESS: #Longpress
      print("Raspberry Pi will shut down...")
      syslog.syslog('Shutdown: System halted');
      args_longpress = shlex.split(COMMAND_LONGPRESS)
      subprocess.call(args_longpress)
    else: #Shortpress
      print("Switching the display output...")
      syslog.syslog('Display: Switch to the other display output');
      args_shortpress = shlex.split(COMMAND_SHORTPRESS)
      subprocess.call(args_shortpress)


BUTTON.wait_for_press()
BUTTON.when_pressed = start_timer
BUTTON.when_released = execute_command


syslog.syslog('changeconfig.py started');
while True:
  try:
    time.sleep(300)
  except KeyboardInterrupt:
    syslog.syslog('Shutdown terminated (Keyboard)');
    print ("Bye bye")
    sys.exit(0)
