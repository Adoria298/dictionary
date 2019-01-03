from dictionary import Dictionary
import csv
import collections

def test_init_no_params():
    test_dict = Dictionary()
    assert test_dict._csv_file == None
    assert test_dict._dictionary == None

def test_init_params():
    test_dict = Dictionary("latin.csv")
    test_dict.parse_csv()
    with open('latin.csv', 'r') as test_csv:
        assert type(test_dict._dictionary) == type(csv.DictReader(test_csv))

def test_search_by_word():
    test_dict = Dictionary("latin.csv")
    result = test_dict.search("puella")
    assert "puella" in result[0]["word"]
