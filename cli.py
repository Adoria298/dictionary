from dictionary import Dictionary
from argparse import ArgumentParser

parser = ArgumentParser(description="Dictionary Lookup")
parser.add_argument(
    'dictionary',   # positional 
    action='store',
    help='Path to Dictionary-compatible csv file.'
)
parser.add_argument(
    'config',
    default='latin.json',
    help='JSON config file.',
    nargs='?'
)
args = parser.parse_args()
dictionary = Dictionary(args.dictionary, args.config)
while True:
    try:
        print(dictionary.formatted_search(input("> ")))
    except KeyboardInterrupt:
        quit(1)