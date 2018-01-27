#!/usr/bin/env python3

from logger.messages import status
from logger.messages import error
from logger.messages import verbose
from logger.messages import warning
from logger import messages
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


def repeated_numbers(first, second, third):
    """TODO: Docstring for repeated.

    :first: TODO
    :second: TODO
    :third: TODO
    :returns: TODO

    """
    repeated = []
    if first == second and first == third:
        repeated.append(first)
        repeated.append(second)
        repeated.append(third)
    elif first == second:
        repeated.append(first)
        repeated.append(second)
    elif first == third:
        repeated.append(first)
        repeated.append(third)
    elif second == third:
        repeated.append(second)
        repeated.append(third)

    return repeated


class Triplet(object):
    """Triplet wrapper"""

    def __init__(self, first, second, third, amount):
        super(Triplet, self).__init__()
        self.first = first
        self.second = second
        self.third = third
        self.amount = amount

    def __str__(self):
        """Representaion of a Triplet
        :returns: TODO

        """
        return "({0}, {1}, {2}):\t\t\t{3}".format(self.first,
                                                  self.second,
                                                  self.third,
                                                  self.amount)

    def fill(self, first, second, third, amount):
        """TODO: Docstring for fill.

        :first: TODO
        :second: TODO
        :third: TODO
        :returns: TODO

        """
        self.first = first
        self.second = second
        self.third = third

        self.amount = amount


class TripletMaker(object):
    """Make triplet of numbers"""

    def __init__(self, array):
        super(TripletMaker, self).__init__()
        if array is None or len(array) < 0:
            raise Exception("WTF man an empty array is not valid")

        self.tree = {}
        for item in range(-100, 101):
            self.tree[item] = 0

        for item in array:
            try:
                if type(item) is str:
                    item = int(item)
                self.tree[item] += 1
            except ValueError as e:
                warning("Not a valid item {0}".format(item))
                continue

        # Don't do this shit if we aren't in debug mode
        if messages.debug_mode:
            self.size = 0
            for key in range(-100, 101):
                value = self.tree[key]
                self.size += value
                verbose("Key: {0};      Value: {1}".format(key, value))
            verbose("size {0}".format(self.size))

        self.size = len(array) - 1
        self.time = None
        self.done = False
        self.triplets = []
        self.domain = list(range(-100, 101))

    def _reduce_to_zero(self, pair_sum):
        """Find if there's the inverse of the first 2 numbers

            if sum = 98 then look for -98
            if sum = -98 then look for 98

        :self.tree: dict, Dictionary with all the numbers
        :pair_sum: int, the sum of the first 2 numbers
        :returns: Bool, True if the inverse exists, False otherwise

        """
        if (pair_sum * -1) in self.tree and self.tree[pair_sum * -1] > 0:
            return True
        return False

    def _find_triplet(self, number, domain):
        """Select the best next number of the triplet
        :returns: int, the number which is also the key of the self.tree dict

        """
        usable = False
        # By default the domain is negative, we can reverse it to use the positive domain
        limits = self.domain if domain < 0 else list(reversed(self.domain))
        verbose("Domain: {0}".format(limits))
        for pair in limits:
            if self.tree[pair] > 0:
                if self._reduce_to_zero(number + pair) is True:
                    repeated = repeated_numbers(number,
                                                pair,
                                                (number + pair) * -1)
                    if len(repeated) != 0 and self.tree[repeated[0]] < len(repeated):
                        continue
                    self._save_triplet(number, pair, (number + pair) * -1)
                    usable = True
                    break

        return usable

    def _remove_numbers(self, first, second, third):
        """Remove the triplet from the dictionary

        TODO: Should we use a vector instead ?

        :self.tree: dict, Dictionary with all the numbers
        :first: int, the first number of the triplet
        :second: int, the first number of the triplet
        :third: int, the first number of the triplet
        :returns: dict, the self.tree with decreased index if the found triplet

        """
        repeated = repeated_numbers(first, second, third)

        minimun = 0
        if len(repeated) == 0:
            verbose("All numbers are different")
            # All numbers are different from each other, so normal triplet
            minimun = min(
                [
                    self.tree[first],
                    self.tree[second],
                    self.tree[third],
                ]
            )

            self.tree[first] -= minimun
            self.tree[second] -= minimun
            self.tree[third] -= minimun
        elif len(repeated) == 3:
            verbose("Using {0} three times with {1} elements".format(repeated[0],
                                                                     self.tree[repeated[0]]))
            # Same number in each case, just "0" can be here
            minimun = (self.tree[first] // 3) * 3
            self.tree[first] -= minimun
        else:
            verbose("Using {0} two times with {1} elements".format(repeated[0],
                                                                   self.tree[repeated[0]]))
            # We have two repeated numbers so need to perform a division
            minimun = min([(self.tree[repeated[0]] // 2), self.tree[first]])

            diff = 0
            if not (first in repeated):
                diff = first
            elif not (second in repeated):
                diff = second
            elif not (third in repeated):
                diff = third

            self.tree[repeated[0]] -= (minimun * 2)
            self.tree[diff] -= minimun

        triplet = Triplet(first, second, third, minimun)

        return triplet

    def _save_triplet(self, first, second, third):
        """TODO: Docstring for _save_triplet.

        :triplet: TODO
        :returns: TODO

        """
        triplet = self._remove_numbers(first, second, third)
        status("Found triplet {0}".format(triplet))
        self.done = False
        self.triplets.append(triplet)

    def start(self):
        """Look for the next triplet of numbers
        :returns: Tuple, Returns a tuple with a vector of the 3 numbers and the
                        updated dictionary, And empty vector is return if no
                        triplet was found
        """
        start_time = time.time()
        while not self.done:
            self.done = True
            for item in range(-100, 101):
                    # Check whether or not we have elements in the next number
                if self.tree[item] > 0:
                    verbose("Looking triplet for {0} with {1} elements".format(item,
                                                                               self.tree[item]))
                    usable = self._find_triplet(item, item * -1)
                    if not usable:
                        verbose("No triplet found for {0}".format(item))
                else:
                    verbose("Skipping {0}: {1}".format(item, self.tree[item]))

        end_time = time.time()

        self.time = end_time - start_time

        status("End time of {0}".format(self.time))

        # Save time by not doing this shit if is not debug mode
        if messages.debug_mode:
            total = 0
            verbose("Unpaird numbers")
            for key in range(-100, 101):
                value = self.tree[key]
                if value > 0:
                    total += value
                    verbose("Key: {0};      Value: {1}".format(key, value))
            verbose("Total {0}".format(total))


if __name__ == "__main__":
    raise Exception(
        "This script is not intended to be used as a standalone script")
