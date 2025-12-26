import re

def censor_text(text, censor_char='*'):
    bad_words = [
        r'хуй',
        r'пизду',
    ]

    censored_text = text

    for pattern in bad_words:
        censored_text = re.sub(
            pattern,
            lambda m: censor_char * len(m.group()),
            censored_text,
            flags=re.IGNORECASE
        )

    return censored_text

text = f'Не тужи, дорогой, и не ахай, \
Жизнь держи, как коня, за узду, \
Посылай всех и каждого на хуй, \
Чтоб тебя не послали в пизду! \
Есенин С. А'

censored = censor_text(text)
print(censored)