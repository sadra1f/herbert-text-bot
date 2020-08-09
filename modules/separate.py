from time import sleep

from modules.spammer import spam


def read_file_lines(path: str) -> list:
    try:
        if path[-4:] == '.txt':
            with open(path, 'r') as target:
                return target.readlines()
    except:
        pass
    return None


def separate_words(text: str, time: int = 1, first_time_delay: bool = False) -> bool:
    text = text.split(' ')

    for word in text:
        if word.strip() != '':
            if first_time_delay:
                sleep(time)
            else:
                first_time_delay = True

        if word.strip() != '' and not spam(word.strip()):
            return False
    return True


def separate_words_file(path: str, time: int = 1) -> bool:
    lines = read_file_lines(path)

    for line in lines:
        if not separate_words(str(line).strip(), time, True):
            return False
    return True


def separate_lines_file(path: str, time: int = 1, first_time_delay = False) -> bool:
    lines = read_file_lines(path)

    for line in lines:
        if line.strip() != '':
            if first_time_delay:
                sleep(time)
            else:
                first_time_delay = True
        
        if line.strip() != '' and not spam(line.strip()):
            return False
    return True
