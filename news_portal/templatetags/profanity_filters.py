from django import template



register = template.Library()

BAD_WORDS =['Telegram','банк','резюме','банк']


@register.filter()
def censor(value):
    if not isinstance(value, str):
        raise ValueError('Нельзя цензурировать не строку')


    for word in BAD_WORDS:
        value = value.replace(word[1:], '*' * (len(word) - 1))
        return value








