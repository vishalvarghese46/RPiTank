import curses
from time import sleep

def main(stdscr):
    curses.curs_set(0)

    while True:
        key = stdscr.getch()
        stdscr.clear()
        if key == curses.KEY_UP:
            stdscr.addstr(0,0, "You pressed up!")
        elif key == curses.KEY_DOWN:
            stdscr.addstr(1,0, "You pressed down!")
        elif key == curses.KEY_LEFT:
            stdscr.addstr(2,0, "You pressed Left!")
        elif key == curses.KEY_RIGHT:
            stdscr.addstr(3,0, "You pressed right!")
        elif key == curses.KEY_ENTER or key in [10, 3]:
            stdscr.addstr(4,0, "You've pressed Enter Key!!")
        stdscr.refresh()
curses.wrapper(main)