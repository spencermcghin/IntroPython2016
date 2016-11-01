# Imports #


# Open file, get rid of breaks, and return as list #

with open('/Users/SMcGhin/Documents/IntroPython2016/students/spencer_mcghin/session4/sherlock_small.txt', 'r') as text:
    doc_list = text.read().split()  # Generate List #
    doc = [" ".join(doc_list).strip('--')]  # Make one long string #


# Validate input against text list and generate following words #

def gen_trigrams():
    input_text = input("Please enter a text string from the document '\n'"
                       "> ")
    input_text = input_text.split()  # convert input_text to list #
    for i in range(0, len(doc_list)-3):  # iterate through the document and find matches for each part of input_text #
        if input_text[0] == doc_list[i] and input_text[1] == doc_list[i + 1]:
            print(doc_list[i + 2])

gen_trigrams()