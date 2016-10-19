import os


def path_print():
    current_dir = os.getcwd()
    for files in current_dir:
        print(os.path.abspath(files))

path_print()