"""
 Напишите функцию, которая будет принимать номер кредитной карты и
показывать только последние 4 цифры. Остальные цифры должны заменяться
звездочками
"""


def hide_card_nums(nums: int):
    if isinstance(nums, int):
        hiden_nums = str (nums)
        if len (hiden_nums) > 16 or len (hiden_nums) < 16 :
            raise ValueError ("Количество введенных символов не соответствует")
        else:
            return f"{hiden_nums.replace(hiden_nums[:12], '*' * 12)}"
    else:
        raise ValueError ('Введенные данные некорректны')


