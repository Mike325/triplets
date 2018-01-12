#!/usr/bin/env python3

import gen_files
import argparse

__header__ = """
                              -`
              ...            .o+`
           .+++s+   .h`.    `ooo/
          `+++%++  .h+++   `+oooo:
          +++o+++ .hhs++. `+oooooo:
          +s%%so%.hohhoo'  'oooooo+:
          `+ooohs+h+sh++`/:  ++oooo+:
           hh+o+hoso+h+`/++++.+++++++:
            `+h+++h.+ `/++++++++++++++:
                     `/+++ooooooooooooo/`
                    ./ooosssso++osssssso+`
                   .oossssso-````/osssss::`
                  -osssssso.      :ssss``to.
                 :osssssss/  Mike  osssl   +
                /ossssssss/   8a   +sssslb
              `/ossssso+/:-        -:/+ossss'.-
             `+sso+:-`                 `.-/+oso:
            `++:.                           `-/+/
            .`                                 `/
"""


def status_message(message):
    """TODO: Docstring for status_message.

    :message: TODO
    :returns: TODO

    """
    print("[*]  {0}".format(message))


def warning_message(message):
    """TODO: Docstring for status_message.

    :message: TODO
    :returns: TODO

    """
    print("[!]  ---- Warning: {0}".format(message))


def error_message(message):
    """TODO: Docstring for status_message.

    :message: TODO
    :returns: TODO

    """
    print("[X]  ---- Error: {0}".format(message))


def __parse_arguments():
    """ Function to parse CLI args
    :returns: object with the CLI arguments

    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="File with the numbers", type=str)
    parser.add_argument("-s", "--seed", help="Seed for the random numbers", type=int)
    parser.add_argument("-v", "--verbose", help="Enable debug messages", type=bool)
    cli_args = parser.parse_args()

    return cli_args


def main():
    """Main function
    """
    cli_args = __parse_arguments()
    pass


if __name__ == "__main__":
    main()
else:
    raise Exception(
        "This script is not intended to be used as a module")
