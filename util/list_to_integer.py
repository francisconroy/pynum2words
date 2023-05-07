import logging


def list_to_integer(digit_list=[]):
    """

    :param digit_list:
    :return: success, integer value if possible otherwise
    """
    if not digit_list:
        return False, None

    if isinstance(digit_list, int):
        digit_list = [digit_list]

    charlist = [str(x) for x in digit_list]
    try:
        return True, int("".join(charlist))
    except ValueError:
        logging.warning(f"Non-integer value given{charlist}")
        return False, None
    except:
        raise()
    return False, None