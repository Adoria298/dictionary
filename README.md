# dictionary

A dictionary look up app designed for the command line user.
An example Latin dictionary is provided, feel free to update as your contribution, or to add other languages.

## usage

At the commandline, run: `python cli.py {dictionary file}`. Ensure the `python` command points to python 3.6 at least. If it does not, but `python3` or `python3.6` do, use them instead. The dictionary file can be any csv file in the format defined below. Included in this repository is a limited Latin dictionary, `latin.csv`. You can use it like with the following command.

`python cli.py latin.csv`

This produces a prompt. 

 `> `

At this prompt you can type your search term.

```md
> puella
1 result found.

puella, puellae
noun - 1d,f
girl

```

To exit, press CTRL+C to produce a KeyboardInterrupt error. There are no `try/except` statements to catch it yet, so you will see a small traceback like the one below.

```python
Traceback (most recent call last):
  File "cli.py", line 30, in <module>
    print(parse_search(input("> "), dicti = dictionary))
KeyboardInterrupt
```

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