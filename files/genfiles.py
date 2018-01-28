#!/usr/bin/env python3

from random import randint
from logger.messages import status
from logger.messages import error
from logger.messages import verbose
import os
import time

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


def get_filename(size):
    """TODO: Docstring for define_name.

    :size: TODO
    :returns: TODO

    """
    filename = ""
    if size >= 1000000:
        filename = "{0}Mnums".format(size // 1000000)
    elif size >= 1000:
        filename = "{0}Knums".format(size // 1000)
    else:
        filename = "{0}nums".format(size)

    return filename


def log_triplets(size, triplets, searchtime, filename=""):
    """TODO: Docstring for log_triplets.

    :output: TODO
    :size: TODO
    :triplets: TODO
    :returns: TODO

    """
    if filename == "":
        filename = get_filename(size) + ".log"

    with open(filename, "w") as log:
        log.write("Triplet\t\tNumber of times found\n\n")
        total = 0
        for triplet in triplets:
            total += triplet.amount
            log.write("{0}\n".format(triplet))

        log.write("\nTotal of triplets\t\t{0}\n".format(total))
        log.write("Different triplets:\t\t{0}\n".format(len(triplets)))
        log.write("Time to find the triplets {0}".format(searchtime))


def gen_files(size=1000, filename="", seed=None):
    """TODO: Docstring for gen_files.

    :size: TODO
    :returns: TODO

    """
    # start_time = time.time()

    if filename == "":
        filename = get_filename(size) + ".txt"

    if seed is not None:
        verbose("Using seed {0}".format(seed))

    with open(filename, "w") as data:
        verbose("Creating {0}".format(filename))
        for x in range(size):
            number = str(randint(-100, 100))
            data.write(number + ',')


def check_files(size=1000, filename="", override=False):
    """TODO: Docstring for check_files.

    :size: TODO
    :returns: TODO

    """

    if filename == "":
        filename = get_filename(size) + ".txt"

    if not os.path.isfile(filename) or override is True:
        if os.path.isfile(filename) and override is True:
            verbose("Removing {0}".format(filename))
        gen_files(size, filename)


def get_array(filename="", size=None):
    """TODO: Docstring for get_array.

    :size: TODO
    :returns: TODO

    """

    if filename == "":
        filename = get_filename(size) + ".txt"

    array = None
    with open(filename, "r") as data:
        status("Searching in {0}".format(filename))
        array = data.read()
        array = array.split(",")

    return array


if __name__ == "__main__":
    check_files()
