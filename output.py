WELCOME_STRING = """****************************************************************************************
****************************************************************************************
-----------------------------WELCOME TO THE JOURNAL-------------------------------------

****************************************************************************************
****************************************************************************************
"""


def create_menu_string(options, journals):
    s = "\nHello sir,\n\nYour Journals:\n"
    s += list_items(journals)
    s += "\nWhat is your wish?\n"
    s += list_items(options)
    return s


def create_journal_menu_string(options, entries, journal):
    s = f"\nHello sir,\nYou are in {journal} Journal\nYour Entries:\n"
    s += list_items(entries)
    s += "\nWhat is your wish?\n"
    s += list_items(options)
    return s


def list_items(ls):
    s = ''
    for i, j in enumerate(ls):
        s += f"{i+1}.{j}\n"
    return s


def create_items_menu(ls, item):
    s = f"\nplease choose {item} by index\n"
    for i, j in enumerate(ls):
        s += f"{i+1}.{j}\n"
    s += "to go back press 0"
    return s


def print_welcome():
    print(WELCOME_STRING)


__all__ = ["print_welcome",
           "create_items_menu", "create_menu_string", "create_journal_menu_string"]
