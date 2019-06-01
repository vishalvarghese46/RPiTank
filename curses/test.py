import curses
import sys

actions = {
    curses.KEY_UP: "Move forward",
    curses.KEY_DOWN: "Move Backward",
    curses.KEY_LEFT: "Move Left",
    curses.KEY_RIGHT: "Move Right",
}



def print(stdscr, action):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    y = h//2
    x = w//2 - len(action)//2
    stdscr.addstr(y,x, action)
    stdscr.refresh()


def main(stdscr):
    curses.curs_set(0)
    nextKey = None
    while True:
        if nextKey is None:
            key = stdscr.getch()
        else:
            key = nextKey
            nextKey = None
        if key != -1:
            action = actions.get(key)
            if action is not None:
                print(stdscr, action)
            nextKey = key
            while nextKey == key:
                nextKey = stdscr.getch()
            print(stdscr, "shit!")
curses.wrapper(main)







