from dictionary import Dictionary
import csv
import collections

def test_init_params():
    test_dict = Dictionary("latin.csv", "latin.json")
    test_dict._parse_csv()
    with open('latin.csv', 'r') as test_csv:
        assert type(test_dict._dictionary) == type(list(csv.DictReader(test_csv)))

def test_search_by_word():
    test_dict = Dictionary("latin.csv", "latin.json")
    result = test_dict.search("puella")
    assert "puella" in result[0]["word"]

def test_format_search():
    test_dict = Dictionary("latin.csv", "latin.json")
    results = test_dict.formatted_search("puella")
    for i in results:
        assert type(i) == type("")