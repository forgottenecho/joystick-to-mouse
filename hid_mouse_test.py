from adafruit_hid.mouse import Mouse
import usb_hid
import time

mouse = Mouse(usb_hid.devices)

while(True):
    mouse.move(x=50, y=50)
    time.sleep(1)
    mouse.move(x=-50, y=-50)
    time.sleep(1)