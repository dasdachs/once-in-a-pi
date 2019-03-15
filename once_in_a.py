#! /usr/bin/env python3
#
# Once in a py
# ------------
#
# On the day my baby was born, flushed with incomprehensible joy, my mind
# wondered of. I somehow started thinking about the fact that PI is endless,
# and that somewhere in the number all the stories, every sentence of
# every person you will (have) ever meet is written. If one uses some encoding that is :)
#
# Once in a py is my small `thank you` for that day. What it does is, it takes
# a random string , converts it to numbers using `ord()` and divides an
# approximation of π until it finds a streek of numbers that match the ordinal
# representation of the lookup string.
#
# Keep in mind that it uses an approximation for π. You can change it, but it
# would still be an approximation .
#
# Contributions are more than welcome.
#
# @dasdachs
# License: MIT 2019
__author__ = "Jani Šumak"
__version__ = "1.0"
import argparse
import sys


def find_lookup_string(lookup_string, pi='355/113'):
    number, divider = [int(num) for num in pi.split('/')]
    string = " ".join(lookup_string)

    string_as_ord = "".join(
        [str(ord(letter)) for letter in string]
    )
    print(f'Looking for {string} ...')
    print(f'... which is {string_as_ord} for a computer')

    current_numbers = ''
    index_of_pi = 0
    to_divide = number % divider

    print(f'Begining search, it might take a while.')
    print(f'Lookup string: {string_as_ord}')
    print('-'*(len(string_as_ord) + 14))

    print()
    while current_numbers != string_as_ord:
        sys.stdout.write('Longest found match: ' + current_numbers)
        index_of_pi += 1
        to_divide *= 10
        current_pi_value = str(to_divide // divider)
        remainder = to_divide % divider
        if current_pi_value == string_as_ord[len(current_numbers)]:
            current_numbers = current_numbers + current_pi_value
        else:
            current_numbers = ''
        to_divide = remainder
        sys.stdout.write('\r')
        sys.stdout.flush()
    index = index_of_pi - len(lookup_string)
    return (string, pi, string_as_ord, index_of_pi)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Find a random unicode string in an aproximation of PI'
    )
    parser.add_argument(
        'lookup_string',
        type=str,
        nargs='+',
        help='The unicode string you want to find'
    )
    parser.add_argument(
        '--pi',
        type=str,
        help='Set your prefered approximation of π (default: 355/113)'
    )
    parser.add_argument(
        '--to',
        type=str,
        help='Path to the file to write the results to.'
    )
    args = parser.parse_args()
    approximation = args.pi if args.pi else '355/113'
    string, pi, string_as_ord, index_of_pi = find_lookup_string(args.lookup_string, approximation)

    if not args.to:
        print(f'Lookup string was found at {index_of_pi}')
        print(f'This is the string as a value of π 3. ... {string_as_ord} ...')
    else:
        with open(args.to, 'w') as f:
            f.write(f'Looking for {lookup_string} in π\n')
            f.write(f'Lookup string was found at {index_of_pi}\n')
            f.write(f'This is the string as a value of π 3. ... {string_as_ord} ...')

