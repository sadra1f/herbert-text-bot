from sys import argv
from os import system, name
from time import sleep

import curses

from modules.spammer import spam

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def arguments() -> list:
    try:
        arg = list(argv[1::])
        arg[0] = arg[0].lower()
        return arg
    except:
        return []

def operation(name: str, arg: list) -> bool:
    if name.lower() == 'spammer' or name.lower() == 's':
        try:
            return spam(arg[0], int(arg[1]), float(arg[2]))
        except:
            try:
                return spam(arg[0], int(arg[1]))
            except:
                return spam(arg[0])
    else:
        False

def start(arg: list):
    clear()
    print('herbert-text-bot:')
    print('(Press \'ctrl + c\' to cancel the operation)\n')
    
    try:
        if str(arg[1]).strip() != '':
            for c in range(5, 0, -1):
                print('\r' + 'Starting... {} '.format(c), end=(''))
                sleep(1)
            print('\r' + (60 * ' '), end='\r')

            print('Started...')
                
            if operation(arg[0], arg[1::]):
                print('Done!')
                return None
    except:
        pass
    clear()
    print('herbert-text-bot:\n\nFailed!')

def menu(option) -> bool:
    clear()
    print('herbert-text-bot:')
    arg = [option]
    try:
        if option == 'about':
            print('\nThis is a simple spammer bot. (for now)\n')
            print('Version: 0.1.0')
            print('GitHub: https://github.com/Sadra1f/herbert-text-bot')
            print('This program is under MIT Licence\n')
        else:
            print('(Press \'ctrl + c\' to cancel the operation)\n')
            if option == 'spammer':
                arg.append(input('Text: '))
                arg.append(input('Count (default: 1): '))
                arg.append(input('Wait time (sec - default: 1): '))
                start(arg)
    except:
        clear()
        print('herbert-text-bot:') 

def mainMenu(stdscr) -> str:

    options = [
        'Spammer',
        'About',
        'Exit'
    ]

    attributes = {}
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    attributes['normal'] = curses.color_pair(1)

    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    attributes['highlighted'] = curses.color_pair(2)

    key = 0
    option = 0  # the current option that is marked

    while key != 10:  # Enter in ascii
        stdscr.erase()
        stdscr.addstr("herbert-text-bot:\n\n", curses.A_NORMAL)

        for index in range(len(options)):
            if index == option:
                attr = attributes['highlighted']
            else:
                attr = attributes['normal']

            if index == len(options) - 2:
                stdscr.addstr('\n')

            stdscr.addstr('- ')
            stdscr.addstr(options[index] + '\n', attr)

        key = stdscr.getch()
        if key == curses.KEY_UP and option > 0:
            option -= 1
        elif key == curses.KEY_DOWN and option < len(options) - 1:
            option += 1

    return str(options[option]).lower()

def main():
    arg = arguments()

    try:
        if arg[0] == 'about':  # main.py spammer 'text' 1 1
            menu(arg[0])
        else:
            start(arg)
    except:
        while True:
            clear()
            option = curses.wrapper(mainMenu)
            if option != 'exit':
                try:
                    menu(option)
                    input('\n(Press \'enter\' to go back)\n')
                except:
                    pass
            else:
                break

if __name__ == "__main__":
    main()
