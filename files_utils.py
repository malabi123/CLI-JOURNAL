import os
from datetime import datetime


def create_dir(path_p, name):
    p = os.path.join(path_p, name)
    if os.path.exists(p):
        return f"\njournal:{name} already exist\n"
    else:
        os.mkdir(p)
        return f"\njournal:{name} created successfully\n"


def delete_dir(path_p, name):
    p = os.path.join(path_p, name)
    if not os.path.exists(p):
        return f"\njournal:{name} doesn't exist\n"
    if os.listdir(p):
        return f"\njournal:{name} doesn't empty, please clear it first"
    else:
        os.rmdir(p)
        return f"\njournal:{name} deleted successfully\n"


def create_ent(path_p, journal, name):
    p = os.path.join(path_p, journal)
    p = os.path.join(p, name)
    if os.path.exists(p):
        return f"\nentry:{name} already exist\n"
    else:
        with open(p, 'w') as f:
            f.write(entry_header(name))
        os.startfile(p)
        return f"\nentry:{name} created successfully\n"


def entry_header(name):
    created_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    title = name.upper()
    padding = 6
    width = len(title) + padding * 2
    divider = "-" * width

    return (
        f"{'#' * width}\n"
        f"{'#' * padding}{title}{'#' * padding}\n"
        f"{'#' * width}\n\n"
        f"Created on: {created_time}\n"
        f"{divider}\n\n"
    )


def delete_ent(path_p, journal, name):
    p = os.path.join(path_p, journal)
    p = os.path.join(p, name)
    if not os.path.exists(p):
        return f"\nentry:{name} doesn't exist\n"
    else:
        os.remove(p)
        return f"\nentry:{name} deleted successfully\n"


def get_all_dir(path):
    ls = [dir.name for dir in os.scandir(path) if dir.is_dir()]
    return ls


def get_entry_str(path_p, journal, name):
    p = os.path.join(path_p, journal)
    p = os.path.join(p, name)
    if not os.path.exists(p):
        return f"\nentry:{name} doesn't exist\n"
    else:
        with open(p, 'r') as f:
            s = f.read()
    return s


def get_all_ent(path, journal):
    p = os.path.join(path, journal)
    ls = [ent.name for ent in os.scandir(p) if not ent.is_dir()]
    return ls


__all__ = ["create_dir", "get_all_dir", "delete_dir",
           "create_ent", "get_all_ent", "get_entry_str", "delete_ent"]
