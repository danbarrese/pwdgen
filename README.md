pwdgen
======

##Description
A random password generator written in Python.  This is my first Python script, and is more or less practice.  Passwords are generated using the `random` module.

##Installation
Run with a Python 3 interpreter.

##Example
Here is example output from the following: `python3 pwdgen.py --length 16 --count 5`:

    PsfUzYotk5OPxuWX
    5XqQvxYZA&u9)eYd
    z5UvJkirMM7rRZ&(
    iot8KSP5OGphy!jK
    VbMkjjNX5(LP7gnY

##Help
```bash
usage: pwdgen.py [-h] [--length L] [--count C] [--first-char X] [--numbers]
                 [--no-numbers] [--alpha-lower] [--no-alpha-lower]
                 [--alpha-upper] [--no-alpha-upper] [--symbols-common]
                 [--no-symbols-common] [--symbols-uncommon]
                 [--no-symbols-uncommon]

Random password generator.

optional arguments:
  -h, --help            show this help message and exit
  --length L, -l L      the number (L) of characters in the generated password
  --count C, -c C       the number (C) of passwords to generate
  --first-char X, -a X  the first character (X) in the generated password
  --numbers             include numbers [0-9]
  --no-numbers          do NOT include numbers [0-9]
  --alpha-lower         include numbers [a-z]
  --no-alpha-lower      do NOT include alphas [a-z]
  --alpha-upper         include numbers [A-Z]
  --no-alpha-upper      do NOT include alphas [A-Z]
  --symbols-common      include common symbols
  --no-symbols-common   do NOT include common symbols
  --symbols-uncommon    include uncommon symbols
  --no-symbols-uncommon
                        do NOT include uncommon symbols
```
