from unittest import TestCase

from nose.tools import assert_equal
from nose_parameterized import parameterized

from questions import (
    get_biggest_and_lowest_value,
    get_consecutive_chars,
    convert_to_roman_numeral,
    reverse_words_in_a_string)


class QuestionsTestCase(TestCase):

    def test_reverse_words_in_a_string(self):
        assert_equal(
            'fox brown quick The',
            reverse_words_in_a_string('The quick brown fox'))

    def test_get_biggest_and_lowest_value(self):
        numbers = [0.34, 7, 90, 3, 0.002, 1, 67]
        assert_equal((0.002, 90), get_biggest_and_lowest_value(numbers))

    def test_get_consecutive_chars(self):
        example = "blaaaablaaa"
        assert_equal('b1l1a4b1l1a3', get_consecutive_chars(example))

    @parameterized.expand([
        (1, 'I'),
        (3, 'III'),
        (4, 'IV'),
        (5, 'V'),
        (6, 'VI'),
        (46, 'XLVI'),
        (90, 'XC'),
        (2014, 'MMXIV'),
        (4000, 'MMMM'),
        (4441, 'MMMMCDXLI'),
    ])
    def test_convert_to_roman_numeral(self, base, output):
        assert_equal(output, convert_to_roman_numeral(base))
