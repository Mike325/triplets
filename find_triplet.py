#!/usr/bin/env python3

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


def _next_number(num_register, num_sign):
    """Select the best next number of the triplet
    :returns: int, the number which is also the key of the num_register dict

    """
    pass


def _reduce_to_zero(num_register, pair_sum):
    """Find if there's the inverse of the first 2 numbers

        if sum = 98 then look for -98
        if sum = -98 then look for 98

    :num_register: dict, Dictionary with all the numbers
    :pair_sum: int, the sum of the first 2 numbers
    :returns: Bool, True if the inverse exists, False otherwise

    """
    if (pair_sum * -1) in num_register:
        return True
    return False


def fill_dictionary(num_register={}, numbers=[]):
    """Create and populate the number dictionary
    :returns: TODO

    """
    if len(num_register) == 0:
        for item in range(-100, 100):
            num_register[item] = 0

    for item in numbers:
        num_register[item] += 1


def remove_numbers(num_register, first, second, third):
    """Remove the triplet from the dictionary

    TODO: Should we use a vector instead ?

    :num_register: dict, Dictionary with all the numbers
    :first: int, the first number of the triplet
    :second: int, the first number of the triplet
    :third: int, the first number of the triplet
    :returns: dict, the num_register with decreased index if the found triplet

    """
    num_register[first] -= 1
    num_register[second] -= 1
    num_register[third] -= 1

    return num_register


def find_triplets(num_register):
    """Look for the next triplet of numbers
    :returns: Tuple, Returns a tuple with a vector of the 3 numbers and the
                     updated dictionary, And empty vector is return if no
                     triplet was found

    """
    pass


if __name__ == "__main__":
    raise Exception(
        "This script is not intended to be used as a standalone script")
