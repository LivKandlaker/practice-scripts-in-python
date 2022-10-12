def square (num):
    """
    The function get number, check if the number is positive and integer
    the function print to the console a square based on the number with "*"
    :param num:
    :return: bool 1/0 (True/False)
    """
    if num > 0 and type(num) == int:
        i = 0
        while i < num:
            if i < 2 or i > (num - 3):
                print( "* " * num)
            else:
                print("* " * 2 + "  " * (num-4) + "* " * 2)
            i += 1
        return 1
    else:
        return 0
    return



