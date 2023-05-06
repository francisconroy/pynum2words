def integer_to_text(integer_in, language="EN"):
    """

    :param language:
    :param integer_in:
    :return: String in the chosen language to represent the word
    """
    return integer_to_words(integer_in, language=language).join(" ")


def integer_to_words(integer_in, language="EN"):
    """

    :param integer_in:
    :param language:
    :return: List of words in the chosen language to represent the number
    """