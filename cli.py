from dictionary import Dictionary
from argparse import ArgumentParser

parser = ArgumentParser(description="Dictionary Lookup")
parser.add_argument('dictionary',   # positional 
                        action='store',
                        help='Path to Dictionary-compatible csv file.')
args = parser.parse_args()
dictionary = Dictionary(args.dictionary)
while True:
    print(dictionary.formatted_search(input("> "))