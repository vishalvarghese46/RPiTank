import curses
from time import sleep

def main(stdscr):
    curses.curs_set(0)
    h, w = stdscr.getmaxyx()
    text = "Hello, World!"

    x = w//2 - len(text)//2;
    y = h//2

    stdscr.addstr(y,x, text)

    stdscr.refresh()
    sleep(3)
curses.wrapper(main)


