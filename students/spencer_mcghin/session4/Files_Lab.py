import tabulate, collections


# # Print absolute path of files in current directory #
# def print_path():
#     for file in os.listdir(os.getcwd()):
#         print(os.path.abspath(file))

# Read students file and generate languages list #
def gen_lang():
    table_set = collections.OrderedDict()
    doc = open('/Users/SMcGhin/Documents/IntroPython2016/Examples/Session01/students.txt')
    data = {"Languages": []}
    for students, languages in doc:
        print(languages)

gen_lang()




