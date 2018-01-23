#!/usr/bin/env python3

from random import randint
from logger.logger import status_msg
from logger.logger import error_msg
from logger.logger import verbose_msg
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


""" Escriba un programa que genere un millon de numeros enteros aleatorios
entre -100 y 100.
1.- Escriba los primero 1,000 en un archivo 1Knums.txt
2.- Escriba los primero 2,000 en un archivo 2Knums.txt
3.- Escriba los primero 5,000 en un archivo 5Knums.txt
4.- Escriba los primero 10,000 en un archivo 10Knums.txt
5.- Escriba los primero 100,000 en un archivo 100Knums.txt
6.- Escriba el millon de numeros en un archivo 1Mnums.txt """


def genFiles(size=1000, seed=None):
    """TODO: Docstring for genfiles.

    :size: TODO
    :returns: TODO

    """
    # start_time = time.time()

    filename = ""
    if size >= 1000000:
        filename = "{0}Mnums.txt".format(size // 1000000)
    elif size >= 1000:
        filename = "{0}Knums.txt".format(size // 1000)
    else:
        filename = "{0}nums.txt".format(size)

    if seed is not None:
        verbose_msg("Using seed {0}".format(seed))

    with open(filename, "w") as data:
        verbose_msg("Creating {0}".format(filename))
        for x in range(size):
            number = str(randint(-100, 100))
            data.write(number + ',')

    # print(x)
    # print("EXE TIME: " + str(time.time() - start_time))


def checkFiles(override=False):
    """TODO: Docstring for checkFiles.

    :size: TODO
    :returns: TODO

    """
    for item in [1000, 2000, 5000, 10000, 100000, 1000000]:

        filename = ""
        if item >= 1000000:
            filename = "{0}Mnums.txt".format(item // 1000000)
        elif item >= 1000:
            filename = "{0}Knums.txt".format(item // 1000)
        else:
            filename = "{0}nums.txt".format(item)

        if not os.path.isfile(filename) or override is True:
            genFiles(item)


def getArray(size=None):
    """TODO: Docstring for getArray.

    :size: TODO
    :returns: TODO

    """
    filename = ""
    if size >= 1000000:
        filename = "{0}Mnums.txt".format(size // 1000000)
    elif size >= 1000:
        filename = "{0}Knums.txt".format(size // 1000)
    else:
        filename = "{0}nums.txt".format(size)

    array = []
    with open(filename, "r") as data:
        verbose_msg("Reading {0}".format(filename))
        array = data.read()
        array = array.split(",")

    return array


if __name__ == "__main__":
    checkFiles()
