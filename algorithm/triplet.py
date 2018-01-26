#!/usr/bin/env python3

from logger.messages import status
from logger.messages import error
from logger.messages import verbose
from logger.messages import warning

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


def log_triplets(filename, triplets=[]):
    """TODO: Docstring for log_triplets.

    :filename: TODO
    :triplets: TODO
    :returns: TODO

    """
    with open(filename, "r") as results:
        pass


def min_element(triplet=[]):
    """Find the minimum element in an triplet

    :triplet: TODO
    :returns: TODO

    """
    num = triplet[0]

    for value in triplet:
        if value < num:
            num = value

    return num


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
        return "({0}, {1}, {2}): {3}".format(self.first,
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

    def __init__(self, array, output="triplet.log"):
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

        total = 0
        for key in range(-100, 101):
            value = self.tree[key]
            total += value
            verbose("Key: {0};      Value: {1}".format(key, value))
        verbose("Total {0}".format(total))

        self.done = False
        self.output = output
        self.triplets = []
        self.positives = list(range(0, 101))
        self.negatives = list(range(-100, 101))

    def _find_triplet(self, number, domain):
        """Select the best next number of the triplet
        :returns: int, the number which is also the key of the self.tree dict

        """
        usable = False
        limits = self.positives if domain >= 0 else self.negatives
        for pair in limits:
            if pair != number and pair in self.tree and self.tree[pair] > 0:
                if self._reduce_to_zero(number + pair) is True:
                    self._save_triplet(number, pair, (number + pair) * -1)
                    usable = True
                    break

        return usable

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

    def _remove_numbers(self, first, second, third):
        """Remove the triplet from the dictionary

        TODO: Should we use a vector instead ?

        :self.tree: dict, Dictionary with all the numbers
        :first: int, the first number of the triplet
        :second: int, the first number of the triplet
        :third: int, the first number of the triplet
        :returns: dict, the self.tree with decreased index if the found triplet

        """
        minimun = min_element(
            [
                self.tree[first],
                self.tree[second],
                self.tree[third],
            ]
        )

        triplet = Triplet(first, second, third, minimun)

        self.tree[first] -= minimun
        self.tree[second] -= minimun
        self.tree[third] -= minimun

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
        while not self.done:
            self.done = True
            for item in range(-100, 101):
                # Check whether or not we have elementes in the next number
                if self.tree[item] > 0:
                    verbose("Looking triplet for {0} with {1} elements".format(item,
                                                                               self.tree[item]))
                    usable = self._find_triplet(item, item)
                    if not usable:
                        usable = self._find_triplet(item, item * -1)
                        if not usable:
                            verbose("No triplet found for {0}".format(item))
                else:
                    verbose("Skipping {0}: {1}".format(item, self.tree[item]))

        total = 0
        for key in range(-100, 101):
            value = self.tree[key]
            if value > 0:
                total += value
                verbose("Key: {0};      Value: {1}".format(key, value))
        verbose("Total {0}".format(total))


if __name__ == "__main__":
    raise Exception(
        "This script is not intended to be used as a standalone script")
