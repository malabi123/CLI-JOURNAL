from output import *
from input import *
from files_utils import *

PATH = r".\Journals"

MAIN_OPTIONS = ("Create Journal", "Enter Journal", "Read Journal",
                "Delete Journal",  "Exit")
IN_JOURNAL_OPTIONS = ("Create Entry", "Delete Entry",
                      "Read Entry", "go back")


def print_main_menu_and_get_all_jour():
    ls = get_all_dir(PATH)
    s = create_menu_string(MAIN_OPTIONS, ls)
    print(s)
    return ls


def input_loop(num_of_options):
    while True:
        try:
            n = choice_input_zero_to_max_validation(num_of_options)
            return n
        except ValueError as e:
            print(e)


def main():
    print_welcome()
    try:
        while True:
            ls = print_main_menu_and_get_all_jour()
            n = input_loop(len(MAIN_OPTIONS))
            match(n):
                case 1:
                    create_journal()
                case 2:
                    enter_journal(ls)
                case 3:
                    read_journal(ls)
                case 4:
                    delete_journal(ls)
                case 5:
                    break
    except (KeyboardInterrupt, EOFError):
        print("\ngoodbye!")
    except Exception as e:
        print(e)


def print_journal_menu_and_get_all_ent(journal):
    ls = get_all_ent(PATH, journal)
    s = create_journal_menu_string(IN_JOURNAL_OPTIONS, ls, journal)
    print(s)
    return (ls)


def journal_menu(journal):
    while True:
        ls = print_journal_menu_and_get_all_ent(journal)
        n = input_loop(len(IN_JOURNAL_OPTIONS))
        match(n):
            case 1:
                create_entry(journal)
            case 2:
                delete_entry(ls, journal)
            case 3:
                read_entry(ls, journal)
                pass
            case 4:
                break


def create_journal():
    journal = input("\nEnter Journal Name: ")
    print(create_dir(PATH, journal))


def choose_item_input_loop_zero_to_max(max):
    while True:
        try:
            n = choice_input_zero_to_max_validation(max)
            return n
        except ValueError as e:
            print(e)


def create_entry(journal):
    entry = input("\nEnter Entry Name: ")
    print(create_ent(PATH, journal, entry))


def enter_journal(ls):
    s = create_items_menu(ls, "journal")
    print(s)
    n = choose_item_input_loop_zero_to_max(len(ls))
    if n == 0:
        return
    else:
        journal_menu(ls[n-1])


def read_journal(ls):
    s = create_items_menu(ls, "journal")
    print(s)
    n = choose_item_input_loop_zero_to_max(len(ls))
    if n == 0:
        return
    else:
        ls_ent = get_all_ent(PATH, ls[n-1])
        for ent in ls_ent:
            print(f"\n{ent}:\n\n{get_entry_str(PATH, ls[n-1], ent)}\n")


def delete_journal(ls):
    s = create_items_menu(ls, "journal")
    print(s)
    n = choose_item_input_loop_zero_to_max(len(ls))
    if n == 0:
        return
    else:
        print(delete_dir(PATH, ls[n-1]))


def read_entry(ls, journal):
    s = create_items_menu(ls, "entry")
    print(s)
    n = input_loop(len(ls))
    if (n == 0):
        return
    else:
        print(f"\nentry:\n{get_entry_str(PATH, journal, ls[n-1])}\n")


def delete_entry(ls, journal):
    s = create_items_menu(ls, "entry")
    print(s)
    n = input_loop(len(ls))
    if (n == 0):
        return
    else:
        print(delete_ent(PATH, journal, ls[n-1]))


if __name__ == "__main__":
    main()
