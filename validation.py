

def min_max_number_validation(min, max, num, name):
    max_number_validation(min, max, num, name)
    min_number_validation(min, num, name)


def max_number_validation(min, max, num, name):
    if (num > max):
        raise ValueError(f"{name} must be not more then {max}")


def is_number_integer_validation(num, name):
    if not isinstance(num, int) or isinstance(num, bool):
        raise ValueError(f"{name} must be an integer")


def is_str_integer_validation(s, name):
    try:
        int(s)
    except:
        raise ValueError(f"{name} must be an integer")


def min_number_validation(min, num, name):
    if (num < min):
        raise ValueError(f"{name} must be at least {min}")


__all__ = ["min_max_number_validation", "min_number_validation",
           "is_number_integer_validation", "is_str_integer_validation", "max_number_validation"]
