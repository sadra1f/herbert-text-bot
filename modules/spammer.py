from time import sleep

import keyboard


def read_file(path: str) -> str:
    try:
        if path[-4:] == '.txt':
            with open(path, 'r') as target:
                return target.read()
    except:
        pass
    return None


def spam(text: str, num: int = 1, time: int = 1) -> bool:
    try:
        for i in range(num):
            keyboard.write(text)
            keyboard.press_and_release('enter')
            if i != num - 1:
                sleep(time)
        return True
    except:
        return False


def spam_file(path: str, num: int = 1, time: int = 1) -> bool:
    text = read_file(path)
    if text:
        return spam(text, num, time)
    else:
        return False
