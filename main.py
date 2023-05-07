from util.digits_to_words import three_digits_to_words
from util.integer_to_thousand_groups import integer_to_thousand_groups
from data.si_units import prefix_lookup

def integer_to_text(integer_in, language="EN"):
    """

    :param language:
    :param integer_in:
    :return: String in the chosen language to represent the word
    """
    retstr = ""
    thousand_groups = integer_to_thousand_groups(integer_in)
    for index, value in enumerate(thousand_groups[::-1]):
        if value == 0:
            continue
        digitlist = list(str(value))
        suffix = prefix_lookup[language].setdefault((index)*3, "")
        retstr = f"{three_digits_to_words(digitlist, language)} {suffix} {retstr}"
    return retstr.strip()



