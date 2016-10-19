import os


# Print absolute path of files in current directory #

def path_print():
    for file in os.listdir(os.getcwd()):
        print(os.path.abspath(file))

