import curses
import sys

menu = ['Home', 'Play', 'Scoreboard', 'Exit']

exit = ['Yes', 'No']

def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()

def exit_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    exitQ = "Are you sure you want to quit?"
    stdscr.addstr(h//3, w//2 - len(exitQ)//2, exitQ)
    for index, row in enumerate(exit):
        x = w//2 - len(exit)//2 + (8 * index)
        y = h//2
        if index == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y,x, row)
    stdscr.refresh()

def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def main(stdscr):
    # turn off cursor blinking
    curses.curs_set(0)

    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # specify the current selected row
    current_row = 0

    # print the menu
    print_menu(stdscr, current_row)

    while 1:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_UP and current_row == 0:
            current_row = len(menu) - 1
        elif key == curses.KEY_DOWN and current_row == len(menu) - 1:
            current_row = 0
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            print_center(stdscr, "You selected '{}'".format(menu[current_row]))
            stdscr.getch()
            # if user selected last row, exit the program
            if current_row == len(menu) - 1:
                exitRow = 0
                exit_menu(stdscr, exitRow)
                while True: #Adding another infinite while loop for exit menu
                    key1 = stdscr.getch()

                    if key1 == curses.KEY_RIGHT and exitRow > 0:
                        exitRow -= 1
                    elif key1 == curses.KEY_RIGHT and exitRow == 0:
                        exitRow = len(exit)-1
                    elif key1 ==curses.KEY_LEFT and exitRow < len(exit)-1:
                        exitRow += 1
                    elif key1 == curses.KEY_LEFT and exitRow == len(exit) - 1:
                        exitRow = 0
                    elif key == curses.KEY_ENTER or key in [10, 13] and exitRow == 0:
                        sys.exit()
                    elif key == curses.KEY_ENT
                        ER or key in [10, 13] and exitRow == 1:
                        break
                    exit_menu(stdscr, exitRow)
        print_menu(stdscr, current_row)

curses.wrapper(main)