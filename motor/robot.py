import curses
from gpiozero import Robot
import sys

robot = Robot(left=(27,24), right=(16,23))

actions = {
    curses.KEY_UP: robot.forward,
    curses.KEY_DOWN: robot.backward,
    curses.KEY_LEFT: robot.left,
    curses.KEY_RIGHT: robot.right,
}
def main(stdscr):
    nextKey = None
    while True:
        curses.halfdelay(1)
        if nextKey is None:
            key = stdscr.getch()
        else:
            key=nextKey
            nextKey=None
        if key!= -1:
            curses.halfdelay(3)
            action = actions.get(key)
            if action is not None:
                action()
            nextKey=key
            while nextKey==key:
                nextKey=stdscr.getch()
                if nextKey==curses.KEY_ENTER or key in [10, 13]:
                    sys.exit()
            robot.stop()
curses.wrapper(main)

