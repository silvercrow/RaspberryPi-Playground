#import evdev
from evdev import InputDevice, categorize, ecodes

#creates object 'device' to store the data
device = InputDevice('/dev/input/event1')

#prints out device info at start
print(device)

#button id from our selfie stick 
selfieStickBtn = 115

#loop and filter by event code and print the mapped label
for event in device.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == selfieStickBtn:
                print("selfie click :D")
