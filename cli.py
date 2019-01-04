from dictionary import Dictionary
from argparse import ArgumentParser

def parse_search(line: str, dicti: Dictionary):
    results = dicti.search(line)
    if len(results) <= 0:
        result_str = "No results found for search: " + line
    else:
        if len(results) == 1: # not elif so the formatting can be easily changed
            result_str = "1 result found."
        else:
            result_str = str(len(results)) + " results found."
        for i in results:
            result_str += f"""

{i['word']}
{i['type']} - {i['data']}
{i['defi']}
            """
    return result_str

if __name__ == "__main__":
    parser = ArgumentParser(description="Dictionary Lookup")
    parser.add_argument('dictionary',   # positional 
                        action='store',
                        help='Path to Dictionary-compatible csv file.')
    args = parser.parse_args()
    dictionary = Dictionary(args.dictionary)
    while True:
        print(parse_search(input("> "), dicti = dictionary))
