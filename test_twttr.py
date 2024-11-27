from twttr import shorten

def test_no_vowels():
    assert shorten("GaeiouG") == "GG"