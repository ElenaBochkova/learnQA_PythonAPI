import pytest

class TestShortPhrase:

    def test_phrase_is_short(self):
        phrase = input("Set a phrase: ")

        assert len(phrase) < 15, f"Phrase's length is {len(phrase)} that is more or equal 15"