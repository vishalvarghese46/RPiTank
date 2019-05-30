import curses
from time import sleep

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)


    h, w = stdscr.getmaxyx()
    text = "Hello, World!"

    x = w//2 - len(text)//2;
    y = h//2

    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(y,x, text)
    stdscr.refresh()
    sleep(3)
    stdscr.attroff(curses.color_pair(1))
curses.wrapper(main)


