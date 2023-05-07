from data.language_support import words as words
from data.si_units import prefix_lookup
from util.list_to_integer import list_to_integer


def three_digits_to_words(three_digit_list, language="EN"):
    """

    :param three_digit_list:
    :return:
    """
    if len(three_digit_list) > 2:
        status, hundreds = list_to_integer(three_digit_list[0])
        HUNDREDS_POWER = 2
        if not status:
            raise ValueError(f"Could not convert hundreds value to integer {three_digit_list}")
        return_string = f"{words[language][hundreds]} {prefix_lookup[language][HUNDREDS_POWER]}"
        last_digits_in_words = two_digits_to_words(three_digit_list[1:])
        if last_digits_in_words:
            return return_string + " and " + last_digits_in_words
        else:
            return return_string

    else:
        return two_digits_to_words(three_digit_list)


def two_digits_to_words(two_digit_list, language="EN"):
    """

    :param language:
    :param two_digit_list:
    :return:
    """
    # Grab the integer
    retval, value = list_to_integer(two_digit_list)
    if not retval:
        raise ValueError(f"Digit list given was not an integer {two_digit_list}")

    if value == 0:
        return ""

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
