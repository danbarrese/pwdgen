# RANDOM PASSWORD GENERATOR
# Author: Dan Barrese (danbarrese.com)
# Version: 1.01
# Description: Yep.  This is my first Python script.
# Skills exemplified in this script:
# * Random number generation
# * Command line interface
# * List comprehension
# * Loops
#
# Update History:
# 2013.12.25 [DRB][1.0]    Initial implementation.
# 2013.12.29 [DRB][1.01]   Defaulted to 10 passwords and length of 5.

import random
import string
import sys
import argparse

# Parse arguments.
parser = argparse.ArgumentParser(description='Random password generator.')
parser.add_argument('--length', '-l', metavar='L', type=int, nargs=1,
                    dest='length', default=[5],
                    help='the number (L) of characters in the generated password')
parser.add_argument('--count', '-c', metavar='C', type=int, nargs=1,
                    dest='count', default=[10],
                    help='the number (C) of passwords to generate')
parser.add_argument('--first-char', '-a', metavar='X', type=str, nargs=1,
                    dest='first_char', default=[None],
                    help='the first character (X) in the generated password')
parser.add_argument('--numbers', dest='do_numbers', action='store_true',
                    help='include numbers [0-9]')
parser.add_argument('--no-numbers', dest='do_numbers', action='store_false',
                    help='do NOT include numbers [0-9]')
parser.set_defaults(do_numbers=True)
parser.add_argument('--alpha-lower', dest='do_alpha_lower', action='store_true',
                    help='include numbers [a-z]')
parser.add_argument('--no-alpha-lower', dest='do_alpha_lower', action='store_false',
                    help='do NOT include alphas [a-z]')
parser.set_defaults(do_alpha_lower=True)
parser.add_argument('--alpha-upper', dest='do_alpha_upper', action='store_true',
                    help='include numbers [A-Z]')
parser.add_argument('--no-alpha-upper', dest='do_alpha_upper', action='store_false',
                    help='do NOT include alphas [A-Z]')
parser.set_defaults(do_alpha_upper=True)
parser.add_argument('--symbols-common', dest='do_symbols_common', action='store_true',
                    help='include common symbols')
parser.add_argument('--no-symbols-common', dest='do_symbols_common', action='store_false',
                    help='do NOT include common symbols')
parser.set_defaults(do_symbols_common=True)
parser.add_argument('--symbols-uncommon', dest='do_symbols_uncommon', action='store_true',
                    help='include uncommon symbols')
parser.add_argument('--no-symbols-uncommon', dest='do_symbols_uncommon', action='store_false',
                    help='do NOT include uncommon symbols')
parser.set_defaults(do_symbols_uncommon=False)
args = parser.parse_args()

# Set arguments to variables.
pwd_len = args.length[0]
pwd_count = args.count[0]
do_numbers = args.do_numbers
do_alpha_lower = args.do_alpha_lower
do_alpha_upper = args.do_alpha_upper
do_symbols_common = args.do_symbols_common
do_symbols_uncommon = args.do_symbols_uncommon

# Define possible sets of characters.
numbers =  ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alphas_lowercase = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'
        , 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
alphas_uppercase = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
symbols_common = [
        '!', '$', '&', '(', ')', '-', '_', '@', '#'
        ]
symbols_uncommon = [
        '%', '\'', '/', ':', ';', '<', '=', '>', '?', '[',
        '\\', ']', '^', '{', '|', '}', '~', '"', '*', '+', ',', '.', '`'
        ]

# Define keyset.
keyset = []
if do_numbers:
    keyset = keyset + numbers
if do_alpha_lower:
    keyset = keyset + alphas_lowercase
if do_alpha_upper:
    keyset = keyset + alphas_uppercase
if do_symbols_common:
    keyset = keyset + symbols_common
if do_symbols_uncommon:
    keyset = keyset + symbols_uncommon

num_pwds_generated = 0
while num_pwds_generated < pwd_count:
    # Define first character in the password.
    first_char = args.first_char[0]
    if first_char is None:
        first_char = random.sample(keyset, 1)[0]

    # Make password.
    pwd_len_counter = 2
    pwd_sequence = [first_char]
    while pwd_len_counter <= pwd_len:
        pwd_sequence.append(random.sample(keyset, 1)[0])
        pwd_len_counter += 1
    pwd_str = ''.join(pwd_sequence)

    # Print password.
    print pwd_str
    num_pwds_generated += 1

