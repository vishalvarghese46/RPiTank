import gpiozero
import curses
from time import sleep
robot = gpiozero.Robot(left=(13, 18), right=(24, 27))

actions = {
        curses.KEY_UP: robot.forward,
        curses.KEY_DOWN: robot.backward,
        curses.KEY_LEFT: robot.left,
        curses.KEY_RIGHT: robot.right,
}

def main(window):
    next_key=None
    while True:
        curses.halfdelay(1)
        if next_key is None:
            key = window.getch()
        else:
            key = next_key
        next_key = None
        if key != -1:
            # KEY PRESSED
            curses.halfdelay(3)
            action = actions.get(key)
            if action is not None:
                action()
            next_key = key
            while next_key == key:
                next_key = window.getch()
        # KEY RELEASED
            robot.stop()
curses.wrapper(main)

