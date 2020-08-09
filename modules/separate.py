from modules.spammer import spam


def separate_words(text: str, time: int = 1) -> bool:
    try:
        text = text.split(' ')

        for word in text:
            if word.strip() != '' and not spam(word.split(), time=time):
                return False
        return True
    except:
        return False
