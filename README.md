# dictionary

A dictionary look up app designed for the command line user.
An example Latin dictionary is provided, feel free to update as your contribution, or to add other languages.

## csv file format

- Should be saved as `.csv`

- Should be excel-compatible

- Headers:

    1. `word`

        - used to store the searchable word

    2. `type`

        - language-specific, usually 'noun', 'verb', etc

    3. `data`

        - any extra data about the word. if there is none, use a dash `-`

    4. `defi`

        - the definition of the word

- delimiter: a comma - `,`

- escape character: a pair of double quotes surrounding the element - `""`