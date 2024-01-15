from django import template

from num2cyrillic import NumberToWords

register = template.Library()


@register.filter()
def convert_number_to_bg_word(number):
    num2bg = NumberToWords()
    number = str(number)
    lev, st = number.split(".")
    lev_word = num2bg.cyrillic(int(lev))
    st_word = num2bg.cyrillic(int(st))
    return f"{lev_word.capitalize()} лв. и {st_word} ст."


if __name__ == "__main__":
    print(convert_number_to_bg_word(312.05))
