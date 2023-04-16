"""
File: Steeplechase.py
Name: Jay Weng
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()


def jump():
    """
    pre-condition:Karel is in front of the wall.
    post-condition:Karel jump over the wall.
    """

    up()
    cross()
    down()


def up():
    """
    pre-condition:Karel is in front of the wall.
    post-condition:Karel is at the upper left,facing north.
    """
   # while not front_is_clear():
   #     turn_left()
   #     move()
   #   turn_right()
    turn_left()
    while not right_is_clear():
        move()


def cross():
    """
    Pre-condition:Karel is at the upper left,facing north.
    Post-condition:Karel is at the upper right,facing south.
    """
    turn_right()
    move()
    turn_right()


def down():
    """
    Pre-condition:Karel is at the upper right,facing south.
    Post-condition:Karel is at the down right,facing east.
    """
    while front_is_clear():
        move()




def turn_right():
    for i in range(3):
        turn_left()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
