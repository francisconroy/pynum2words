from util.digits_to_words import three_digits_to_words
from util.integer_to_thousand_groups import integer_to_thousand_groups
from data.si_units import

def integer_to_text(integer_in, language="EN"):
    """

    :param language:
    :param integer_in:
    :return: String in the chosen language to represent the word
    """
    retstr = ""
    for index, value in enumerate(integer_to_thousand_groups(integer_in)[::-1]):
        digitlist = list(str(value))
        retstr = f"{three_digits_to_words(digitlist, language)} {} {retstr}"



