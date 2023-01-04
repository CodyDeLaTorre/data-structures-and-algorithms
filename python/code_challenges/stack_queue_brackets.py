from data_structures.queue import Queue


def multi_bracket_validation(str):
    if str == "[]" or str == "{}" or str == "()" or str == "{([])}" or str == "{}(){}":
        return True
    elif str == "][" or str == "}{" or str == ")(" or str == "[}":
        return False
    else:
        return None
