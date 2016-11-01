# Imports #

from random import randint

# Open file, get rid of breaks, and return as list #

with open('/Users/SMcGhin/Documents/IntroPython2016/students/spencer_mcghin/session4/sherlock_small.txt', 'r') as text:
    doc_list = text.read().split()  # Generate List #
    doc = [" ".join(doc_list)]  # Make one long string #

# Input string and generate

def sherlock_trigram():
    n = input("Please enter a random piece of text from the story.'\n'"
              "> ")
    if n in doc_list:
        print(n + " " + doc_list[randint(doc_list.index(n) - 1, doc_list.index(n) + 1)])
    else:
        sherlock_trigram()


sherlock_trigram()
