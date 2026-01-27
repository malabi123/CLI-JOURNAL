from validation import *

MIN_SIZE = 1
g_size = 0


def set_size(size):
    global g_size
    is_number_integer_validation(g_size, "Size")
    min_number_validation(MIN_SIZE, size, "Size")
    g_size = size


def choice_input_and_validation():
    global g_size
    s = input("")
    is_str_integer_validation(s, "index")
    n = int(s)
    min_max_number_validation(MIN_SIZE, g_size, n, "index")
    return n


def choice_input_zero_to_max_validation(max):
    s = input("")
    is_str_integer_validation(s, "index")
    n = int(s)
    min_max_number_validation(0, max, n, "index")
    return n


__all__ = ["choice_input_and_validation", "set_size",
           "choice_input_zero_to_max_validation"]
