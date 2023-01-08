# Passing arguments to Python scripts
This is a simple script example for passing arguments into a Python script file from the command line.

Here we provide two examples, the first using the not-so favoured [getopt](https://docs.python.org/3/library/getopt.html) (a C style parser) whilst the second uses the more widely accepted [argparse](https://docs.python.org/3/library/argparse.html). Both are contained within the [Python standard library](https://docs.python.org/3/library/index.html).

The examples used here are for a basic program that takes the following inputs and also produces some help message:

- `-i` or `--input`
- `-o` or `--output`
- `-u` or `--user`

## Prerequisites
The following prerequisites are required for these programs to execute as intended:

- [Python 3](https://www.python.org/downloads/)

### Passing with getopt
Per the documentation, getopt helps parse command line arguments in [sys.argv](https://docs.python.org/3/library/sys.html?highlight=sys%20argv#sys.argv). It supports Unix style conventions such as special meanings of arguments in the form of `-` and `--`.

This program is run as `python getopt-example.py` followed by any, or all, of the available options.

Note that I have included `try` and `except` statements to handle incorrect usage options. For example, if you pass in `-a` the program will throw an exception printing the error along with the valid usage options. The exception handler makes use of the [GetOptError](https://docs.python.org/3/library/getopt.html#getopt.GetoptError) function.

You must include the short options (-u, -i, -o for example) and each needs to be accompanied by a trailing colon (`:`). Alternatively short options can be an empty string if you do not wish to support short options.

The getopt function also supports long options, this must be a list of strings representing the supported options. Long options also require the argument is followed by an equal (`=`) sign.

### Passing with argparse
Using [argparse](https://docs.python.org/3/library/argparse.html) provides many convenience features.

Firstly, there's no need to build much by way of help logic. The module gives you help messages automatically. You can provide specific help messages with `help="some useful message"` when declaring your argument.

The module is built around an instance of ArgumentParser. Adding your arguments is as simple as assigning an instance to a variable (i.e. `parser = argparse.ArgumentParser`) and then calling `add_argument` (i.e. `parser.add_argument(opts)`).

To run the example program, execute `python argparse-example.py` from your shell with any or all of the arguments.

One of the other convenience functions baked into argparse is the ability to handle invalid arguments out of the box. For example, if you pass in `-a` the program will throw an uncrecognized arguments error. There was no need to handle this via a `try` and `except` clause.

When calling add_argument, you must declare the argument name as a minimum (this would be a positional argument). Additionally you can declare options that take a value (as I have in the example app, such as `-u` and `--username`).

You may also notice that I have added some more information about the program name, its purpose, and some footnote details. Again, all using convenience functions.

Given the many features you get out of the box, and the simplicity for interacting with the parser, you can see why this is the favoured approach to passing arguments at the command line.

## Summary
If you are familiar with C style parsers, getopt may work very well for you.

However if you are unfamiliar with C style parers, or have limited experience with parsers in general, using argparse is the logical choice.