from sys import argv
from os import system, name
from time import sleep

import curses

from modules.spammer import spam, spam_file
from modules.separate import separate_lines_file, separate_words, separate_words_file

title = 'herbert-text-bot:'


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


def get_index(l: list, index: int = 0, t: str = 'str', default=None) -> str:
    try:
        if t.lower() == 'int':
            return int(l[index])
        elif t.lower() == 'float':
            return float(l[index])
        else:
            return l[index]
    except:
        return default


def operation(name: str, arg: list) -> bool:
    if name.lower() == 'spammer' or name.lower() == 's':
        return spam(get_index(arg, 0), get_index(arg, 1, 'int', default=1), get_index(arg, 2, 'float', default=1))

    elif name.lower() == 'filespammer' or name.lower() == 'fs':
        return spam_file(get_index(arg, 0), get_index(arg, 1, 'int', default=1), get_index(arg, 2, 'float', default=1))

    elif name.lower() == 'separatedwords' or name.lower() == 'sw':
        return separate_words(get_index(arg, 0), get_index(arg, 1, 'float', default=1))

    elif name.lower() == 'fileseparatedwords' or name.lower() == 'fsw':
        return separate_words_file(get_index(arg, 0), get_index(arg, 1, 'float', default=1))

    elif name.lower() == 'fileseparatedlines' or name.lower() == 'fsl':
        return separate_lines_file(get_index(arg, 0), get_index(arg, 1, 'float', default=1))

    else:
        return False


def start(arg: list):
    clear()
    print(title)
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
    print(title, '\n\nFailed!')


def menu(option) -> bool:
    clear()
    print(title)
    arg = [option]
    try:
        if option == 'about':
            print('\nThis is a simple spammer bot. (for now)\n')
            print('Version: 0.2.0')
            print('GitHub: https://github.com/Sadra1f/herbert-text-bot')
            print('This program is under MIT Licence\n')
        else:
            print('(Press \'ctrl + c\' to cancel the operation)\n')
            if option == 's':
                arg.append(input('Text: '))
                arg.append(input('Count (default: 1): '))
                arg.append(input('Wait time (sec - default: 1): '))
                start(arg)
            elif option == 'fs':
                arg.append(input('File path (*.txt): '))
                arg.append(input('Count (default: 1): '))
                arg.append(input('Wait time (sec - default: 1): '))
                start(arg)
            elif option == 'sw':
                arg.append(input('Text: '))
                arg.append(input('Wait time (sec - default: 1): '))
                start(arg)
            elif option == 'fsw' or option == 'fsl':
                arg.append(input('File path (*.txt): '))
                arg.append(input('Wait time (sec - default: 1): '))
                start(arg)
    except:
        clear()
        print(title)


def main_menu(stdscr) -> str:

    options = [
        'Spam',
        'Spam from File',
        'Separated Words',
        'Separated Words from File',
        'Separated Lines from File',
        'About',
        'Exit'
    ]

    options_code = [
        's',
        'fs',
        'sw',
        'fsw',
        'fsl',
        'about',
        'exit'
    ]

    attributes = {}
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    attributes['normal'] = curses.color_pair(1)

    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    attributes['highlighted'] = curses.color_pair(2)

    key = 0
    option = 0  # the current option that is marked

    while key != 10:  # Enter in ascii
        try:
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
        except:
            return 'error'

    return str(options_code[option]).lower()


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
            option = curses.wrapper(main_menu)
            if option == 'error':
                print("ERROR: Can't draw the menu! (Try re-opening program in a bigger window)")
                return None
            elif option != 'exit':
                try:
                    menu(option)
                    input('\n(Press \'enter\' to go back)\n')
                except:
                    pass
            else:
                break


if __name__ == "__main__":
    main()
