from sys import argv
from os import system, name
from time import sleep

from modules.spammer import spam

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def arguments() -> list:
    try:
        return argv[1::]
    except:
        return []

def start():    
    clear()
    print('herbert-text-bot:\n')
    
    try:
        arg = argv

        if str(arg[1]).strip() != '':
            for c in range(5, 0, -1):
                print('\r' + 'Starting... {} (Press \'ctrl + c\' to cancel the operation) '.format(c), end=(''))
                sleep(1)
            print('\r' + (60 * ' '), end='\r')

            print('Started...')

            s = None
            try:
                s = spam(arg[1], int(arg[2]))
            except:
                s = spam(arg[1])
                
            if s:
                print('Done!')
                return None
    except:
        pass
    clear()
    print('herbert-text-bot:\n\nFailed!')

def menu():
    pass

def main():
    arg = arguments()

    try:
        if arg[0]:
            start()
    except:
        menu()

if __name__ == "__main__":
    main()
