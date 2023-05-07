from data.language_support import words as words
from data.si_units import prefix_lookup
from util.list_to_integer import list_to_integer


def three_digits_to_words(three_digit_list, language="EN"):
    """

    :param three_digit_list:
    :return:
    """
    status, hundreds = list_to_integer(three_digit_list[0])
    HUNDREDS_POWER = 2
    if not status:
        raise ValueError(f"Could not convert hundreds value to integer {three_digit_list}")

    return_string = f"{words[language][hundreds]} {prefix_lookup[language][HUNDREDS_POWER]}"
    return return_string + " and " + two_digits_to_words(three_digit_list[1:])


def two_digits_to_words(two_digit_list, language="EN"):
    """

    :param two_digit_list:
    :return:
    """
    # Grab the integer
    retval, value = list_to_integer(two_digit_list)
    if not retval:
        raise ValueError(f"Digit list given was not an integer {two_digit_list}")

    if language not in words:
        raise ValueError(f"Language selected not supported {language}")

    if value in words[language]:
        return words[language][value]

    if 10 < value < 20:
        second_digit = list_to_integer(two_digit_list[1])
        return second_digit.strip("t") + "teen"

    if value > 20:
        tens = int(str(value)[0] + "0")
        second_digit = int(str(value)[1])
        return f"{words[language][tens]} {words[language][second_digit]}"
