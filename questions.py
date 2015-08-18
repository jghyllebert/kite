import itertools
import math


def reverse_words_in_a_string(given_string):
    split_string = given_string.split()
    split_string.reverse()
    return ' '.join(split_string)


def get_biggest_and_lowest_value(number_list):
    number_list.sort()
    return number_list[0], number_list[-1]


def get_consecutive_chars(sentence):
    mapping = [[k, len(list(g))] for k, g in itertools.groupby(sentence)]
    return ''.join(['{}{}'.format(k, g) for k, g in mapping])


def convert_to_roman_numeral(number):
    result = ''
    numerals = [
        ('M', 1000),
        ('CM', 900),
        ('D', 500),
        ('CD', 400),
        ('C', 100),
        ('XC', 90),
        ('L', 50),
        ('XL', 40),
        ('X', 10),
        ('V', 5),
        ('I', 1)
    ]

    for index, (numeral, weight) in enumerate(numerals):
        if weight <= number:
            amount = math.floor(number / weight)
            if amount > 3 and index != 0:  # Allows more than one 'M'
                previous_numeral, previous_weight = numerals[index-1]
                remainder = convert_to_roman_numeral(previous_weight - number)
                result += remainder + previous_numeral
                number -= previous_weight - number
            else:
                result += str(numeral * int(amount))
                number -= weight * amount
    return result
