PORT = '/dev/cu.usbmodem142301'
import time

if __name__ == '__main__':
    import pyfirmata

    # Setup pyFirmata
    BOARD = pyfirmata.Arduino(PORT)

    # Setup pins
    pins = [
        None,  # no pin 0
        None,  # no pin 1
        BOARD.get_pin('d:2:s'),  # motor 2
        BOARD.get_pin('d:3:s'),  # motor 3
        BOARD.get_pin('d:4:s'),  # motor 4
        BOARD.get_pin('d:5:s'),  # motor 5
        BOARD.get_pin('d:6:s'),  # motor 6 - vertical thruster
        BOARD.get_pin('d:7:s'),  # motor 7 - vertical thruster
        BOARD.get_pin('d:8:s'),  # motor 8 - claw
        BOARD.get_pin('d:9:s'),  # motor 9
        BOARD.get_pin('d:10:s'),  # motor 10
        None,  # no pin 11
        BOARD.get_pin('d:12:s'),  # motor 12
    ]
    '''All pins are put into a list
    so that they can conveniently be referred to
    via pins[pin num]
    example: pins[8].write(150)
    '''

def sweep_up():
    pos = 0
    while pos<180:
        pins[9].write(pos)
        pos += 1
        time.sleep(.002)

def sweep_down():
    pos = 0
    while pos>0:
        pins[9].write(pos)
        pos -= 1
        time.sleep(.002)

"""
pos = 0
while True:
    while pos<180:
        pins[9].write(pos)
        pos += 1
        time.sleep(.002)
        
    while pos>0:
        pins[9].write(pos)
        pos -= 1
        time.sleep(.002)
"""
        
import pygame

pygame.init()

for i in range(pygame.joystick.get_count()):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()

up_pressed = False
down_pressed = False

pos = 0
while True:
    for event in pygame.event.get(): # User did something.

        if event.type == pygame.JOYBUTTONDOWN and joystick.get_button(7)==1:
            up_pressed = True
            print("up pressed")
        if event.type == pygame.JOYBUTTONDOWN and joystick.get_button(6)==1:
            down_pressed = True
            print("down pressed")

        if event.type == pygame.JOYBUTTONUP and joystick.get_button(7)==0:
            up_pressed = False
            # print(pressed['LT'])
        if event.type == pygame.JOYBUTTONUP and joystick.get_button(6)==0:
            down_pressed = False
            # print(pressed['RT'])

    if up_pressed == True and pos < 180:
        pins[9].write(pos)
        pos += 1
        time.sleep(.005)

    if down_pressed == True and pos > 0:
        pins[9].write(pos)
        pos -= 1
        time.sleep(.005)

        
