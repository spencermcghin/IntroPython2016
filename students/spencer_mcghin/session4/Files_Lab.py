import numpy, collections


# Print absolute path of files in current directory #

def print_path():
    for file in os.listdir(os.getcwd()):
        print(os.path.abspath(file))

# Read students file and generate languages list #

def gen_lang():
    doc = list(open('/Users/SMcGhin/Documents/IntroPython2016/Examples/Session01/students.txt', 'r'))
    data = []
    for line in doc:
        students, languages = line.strip().split(':')
        data.append(languages)
        print(data)



gen_lang()




