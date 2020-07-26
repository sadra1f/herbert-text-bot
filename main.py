from sys import argv
from os import system, name
from time import sleep

from modules.spammer import spam

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def main():
    try:
        arg = argv
        clear()

        if str(arg[1]).strip() != '':
            for c in range(5, 0, -1):
                print('herbert-text-bot:\n\nStarting... {} (Press \'ctrl + c\' to cancel the operation)'.format(c))
                sleep(1)
                clear()

            print('herbert-text-bot:\n\nStarted...')

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

if __name__ == "__main__":
    main()
