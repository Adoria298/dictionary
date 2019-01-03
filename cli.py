from dictionary import Dictionary
from argparse import ArgumentParser

def parse_search(line: str, dicti: Dictionary):
    return dicti.search(line)

if __name__ == "__main__":
    parser = ArgumentParser(description="Dictionary Lookup")
    parser.add_argument('--dictionary', '-d',   # flags 
                        dest='dictionary', 
                        action='store',
                        help='Path to Dictionary-compatible csv file.')
    args = parser.parse_args()
    print(args)