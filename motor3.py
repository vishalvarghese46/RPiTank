from gpiozero import Robot
import curses
import sys
robot = Robot(left=(27,24), right=(16,23))

def main(stdscr):
    while True:
        key = stdscr.getch()
        if key == curses.KEY_UP:
            robot.forward()
        elif key == curses.KEY_DOWN:
            robot.backward()
        elif key == curses.KEY_RIGHT:
            robot.right()
        elif key == curses.KEY_LEFT:
            robot.left()
        elif key == curses.KEY_ENTER or key in [10, 13]:
            sys.exit()
curses.wrapper(main)




