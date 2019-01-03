import csv
import os

class Dictionary:
    """
Wrapper around a csv file in with the following headers:
    - word - the word to be defined
    - type - the type of word it is (e.g. noun, verb, etc)
    - data - extra information (e.g. gender, denclension, etc)
    - defi - the *defi*nition of the word.
"""
    def __init__(self, file=None):
        self._csv_file = file
        if self._csv_file is not None:
            self._open(file)
            self._dictionary = self._parse_csv()
        else:
            self._dictionary = None

    def _open(self, file):
        """
Optional method. Used to initialise dictionary.
Will be called during __init__ if a file parameter is supplied to __init__.
Calls _parse_csv.

Params:
    file: str = a csv file with headers as described above.
"""
        if file is None:
            if self._csv_file is not None:
                self._open(self._csv_file)
            else:
                raise ValueError("file is None")
        elif not os.path.exists(file):
            raise FileNotFoundError(str(file))
        else: 
            self._csv_file = _open(file, "r")



    def _parse_csv(self):
"""
Creates a csv.DictReader object.
"""
        self._dictionary = csv.DictReader(self._csv_file)
        return self._dictionary

    def search(self, term):
        """
Returns all elements in the dictionary which have a word the same as the search 
term, as a list of ordered dicts.

Params:
    term: str = a search term.
"""
        results = []
        for definition in self._dictionary:
            if term in definition["word"]:
                results.append(definition)
        return results

