from pygame import joystick, event, JOYAXISMOTION
import pygame

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
while 1:
    e=event.get()
    # if e.type == JOYAXISMOTION:
        # print('hello')
    axis=0
    value=stick.get_axis(axis)
    # value=stick.get_hat(axis)
    if value:
        print(value)