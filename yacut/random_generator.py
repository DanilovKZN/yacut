from random import choices
from string import ascii_lowercase, ascii_uppercase, digits


def get_unique_short_id():
    """Генерация случайной ссылки из букв разного регистра 
    и цифр в количестве 6 символов."""
    all_symbols = list(digits) + list(ascii_lowercase) + list(ascii_uppercase)
    result_list = choices(all_symbols, k=6)
    return ''.join(result_list)
