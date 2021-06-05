from pygame import joystick, event, JOYAXISMOTION
import pygame
import mouse

pygame.init()

joystick.init()
print(joystick.get_count())
stick=joystick.Joystick(0)
stick.init()
print(stick.get_numaxes())
print(stick.get_numballs())
print(stick.get_numhats())
print(stick.get_numbuttons())
# event.init(, 11)
x=0
y=0
last_state=[0,0]
slow_factor=.1
threshold=.1*slow_factor
mouse.move(x,y)
while 1:
    e=event.get()
    for i in range(stick.get_numbuttons()):
        if stick.get_button(i) == 1:
            print(i)
    value=stick.get_axis(axis)
    if value:
        print(value)  
