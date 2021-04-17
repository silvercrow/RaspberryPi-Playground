#python-evdev allows you to read and write input events on Linux https://python-evdev.readthedocs.io/en/latest/
import evdev
device = evdev.InputDevice('/dev/input/event1')
print(device)
# looping connected devices events
for event in device.read_loop():
  if event.type == evdev.ecodes.EV_KEY:
    print(evdev.categorize(event))