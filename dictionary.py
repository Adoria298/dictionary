import csv
import os
import json

class Dictionary:
    """
Wrapper around a csv file in with the following headers:
    - word - the word to be defined
    - type - the type of word it is (e.g. noun, verb, etc)
    - data - extra information (e.g. gender, denclension, etc)
    - defi - the *defi*nition of the word.

lang_config is a JSON file with the following information:
    - lang - the language name can to e used to find the csv file (a string)
    - data_defs - human-readable replacements for a formatted data section 
                - in this way: 
                ````json
                {
                    "{data shorthand}": "{nice replacement}",
                    ...
                }
                ````

For an example for these two types of file, see latin.csv and latin.json
"""
    def __init__(self, file, lang_config):
        self._csv_file = file
        self._config = lang_config
        self._find_config()

        if self._csv_file is not None:
            self._open(self._csv_file)
            self._dictionary = self._parse_csv()
        else:
            if self._config.get('lang', None) is None:
                self._dictionary = None
            else:
                lang = str(self._config.get('lang'))
                if os.path.exists(lang+'.csv'):
                    self._open(lang+'.csv')
                    self._dictionary = self._parse_csv()
                else:
                    self._dictionary=None        


    def _find_config(self):
        """
Loads language configuration. If not found, defaults are assumed.
        """
        if self._config is not None:
            if self._config.split('.')[-1] == 'json':
                self._config = json.load(open(self._config))
            else:
                raise ValueError('File type not supported: ' + str(self._config))
        else:
            self._config = {}

    def _open(self, file):
        """
Used to initialise dictionary.
Will be called during __init__.

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
            self._csv_file = open(file, "r")



    def _parse_csv(self):
        """
Creates a csv.DictReader object.
"""
        self._dictionary = list(csv.DictReader(self._csv_file))
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

    def formatted_search(self, term):
        """
Formats search results. Wraps around self.search

Params:
    term: str = a search term.
"""
        results = self.search(term)
        if len(results) <= 0:
            result_str = "No results found for search: " + term
        else:
            if len(results) == 1: # not elif so the formatting can be easily changed
                result_str = "1 result found."
            else:
                result_str = str(len(results)) + " results found."
            for i in results:
                result_str += self._format_word(i)
        return result_str

    def _format_word(self, word_defi):
        word = word_defi["word"]
        word_type = word_defi["type"]
        if (word_defi["data"] == '-' 
            or word_defi["data"] == '- '
            or word_defi["data"] == ' -'
            or word_defi["defi"] == ' - '):
                word_data = ""
        else:
            word_data = "- "
            for index, datum in enumerate(word_defi["data"].split(',')):
                word_data += self._config.get("data_defs").get(datum, datum) # if the datum has a definition, use it, otherwise use the datum
                if len(word_defi['data'].split(',')) > 1:
                    if not len(word_defi['data'].split(','))-1 == index:
                        word_data += ', '

        defi = word_defi["defi"]
        return """
{word}
{type} {data}
{defi}
""".format(word=word, type=word_type, data=word_data, defi=defi)