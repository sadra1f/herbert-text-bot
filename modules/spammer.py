from time import sleep

import keyboard

def spam(text: str, num: int = 1, time: int = 1) -> bool:
    try:
        for _ in range(num):
            sleep(time)
            keyboard.write(text)
            keyboard.press_and_release('enter')
        return True
    except:
        return False
        