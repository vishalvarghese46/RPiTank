'''
- Basically sambavam oru terminal canvas ann
- You can control the cursor on the terminal
- installation:
    pip install windows-curses
'''
from time import sleep
import curses

def main(stdscr):
    curses.curs_set(0)
    stdscr.addstr(5,5, "Hello")
    stdscr.refresh()
    sleep(3)

curses.wrapper(main)

'''
Main function'il ittathinte udesham enthan enn vechal oru try catch scene ann,
pakuthi vech program crash ayal terminal changes reset ayikolm
'''