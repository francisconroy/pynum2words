def integer_to_thousand_groups(in_integer):
    """
    :param in_integer:
    :return: groups of three digits
    """
    outgroups = []
    if not isinstance(in_integer, int):
        raise TypeError(f"In integer is not an integer! {in_integer}")
    strval = str(in_integer)

    hanging = len(strval) % 3
    if hanging:
        outgroups.append(strval[0:hanging])

    remaining = strval[hanging:]
    for i in range(0, len(remaining), 3):
        outgroups.append(remaining[i:i + 3])
    return [int(x) for x in outgroups]
