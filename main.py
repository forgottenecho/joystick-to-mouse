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
    # if e.type == JOYAXISMOTION:
        # print('hello')
    dx=stick.get_axis(0)*slow_factor
    dy=stick.get_axis(1)*slow_factor
    if abs(dx) < threshold:
        dx=0
    if abs(dy) < threshold:
        dy=0
    # print('{}, {}'.format(x,y))
    x+=dx
    y+=dy
    if x < 0:
        x-=dx
    if y < 0:
        y-=dy
    mouse.move(x,y)
    
    current_state=[stick.get_button(0),0]
    if current_state[0] and last_state[0] == 0:
        mouse.press(button='left')
        # print('press')
    if current_state[0] == 0 and last_state[0] == 1:
        mouse.release(button='left')
        # print('release')
    last_state=current_state.copy()
    # for i in range(stick.get_numbuttons()):
        # if stick.get_button(i) == 1:
            # print(i)
    # value=stick.get_axis(axis)
    # value=stick.get_hat(axis)
    # if value:
        # print(value)  