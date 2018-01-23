#!/usr/bin/env python3

from random import randint
from logger.logger import status_msg
from logger.logger import error_msg
from logger.logger import verbose_msg

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


def min_element(triplet={}):
    """Find the minimum element in an triplet

    :triplet: TODO
    :returns: TODO

    """
    num = triplet.keys()[0]
    elements = triplet[num]

    for key, value in triplet.items():
        if value < elements:
            num = key
            elements = value

    return (num, elements)


def _save_triplet(triplet):
    """TODO: Docstring for _save_triplet.

    :triplet: TODO
    :returns: TODO

    """
    pass


class Number(object):
    """Number class to wrap values and usable flags"""

    def __init__(self, value=0, usable=False):
        super(Number, self).__init__()
        self.value = value
        self.usable = usable

    def _am_i_usable(self, new_value):
        """TODO: Docstring for _am_i_usable.
        :returns: TODO

        """
        return (self.value + new_value) > 0

    def __add__(self, onumber):
        """Adds the value to the object

        :value: TODO
        :returns: TODO

        """

        try:
            self.usable = self._am_i_usable(onumber.value)
            return Number(self.value + onumber.value, self.usable)
        except AttributeError as e:
            # Since we are dealing with numbers
            self.usable = self._am_i_usable(onumber)
            return Number(self.value + onumber, self.usable)

    def __radd__(self, onumber):
        """Adds the value to the object

        :value: TODO
        :returns: TODO

        """
        try:
            self.usable = self._am_i_usable(onumber.value)
            return Number(self.value + onumber.value, self.usable)
        except AttributeError as e:
            # Since we are dealing with numbers
            self.usable = self._am_i_usable(onumber)
            return Number(self.value + onumber, self.usable)

    def __lt__(self, onumber):
        """Compare operator

        :onumber: TODO
        :returns: TODO

        """
        try:
            return self.value < onumber.value
        except AttributeError as e:
            # Since we are dealing with numbers
            return self.value < onumber

    def __gt__(self, onumber):
        """TODO: Docstring for __gt__.

        :onumber: TODO
        :returns: TODO

        """
        try:
            return self.value > onumber.value
        except AttributeError as e:
            # Since we are dealing with numbers
            return self.value > onumber

    def __eq__(self,  onumber):
        """TODO: Docstring for __eq__.

        :onumber: TODO
        :returns: TODO

        """
        try:
            return self.value == onumber.value
        except AttributeError as e:
            # Since we are dealing with numbers
            return self.value == onumber

    def __str__(self):
        """String representation
        :returns: TODO

        """
        return "{0}".format(self.value)


class Triplet(object):
    """Triplet wrapper"""

    def __init__(self, numbers=[], amount=0):
        super(Triplet, self).__init__()
        self.numbers = numbers
        self.amount = amount

        if:
            pass

    def __str__(self):
        """Representaion of a Triplet
        :returns: TODO

        """
        return "({0}, {1}, {2}): {3}".format(self.numbers[0],
                                             self.numbers[1],
                                             self.numbers[2],
                                             self.amount)

    def complete(self):
        """Tells if a triplet is complete

        :returns: TODO

        """
        return len(self.numbers) == 3

    def fill(self, first, second, third, amount):
        """TODO: Docstring for fill.

        :first: TODO
        :second: TODO
        :third: TODO
        :returns: TODO

        """
        self.numbers.append(first)
        self.numbers.append(second)
        self.numbers.append(third)

        self.amount = amount


class TripletMaker(object):
    """Make triplet of numbers"""

    def __init__(self, array, output="triplet.log"):
        super(TripletMaker, self).__init__()
        if array is None or len(array) < 0:
            raise Exception("WTF man an empty array is not valid")

        for item in range(-100, 101):
            self.tree[item] = Number()

        for item in array:
            try:
                if type(item) is str:
                    item = int(item)
                self.tree[item] += 1
            except ValueError as e:
                continue

        self.output = output
        self.triplets = []

    def _look_positive(self, number):
        """TODO: Docstring for _look_positive.

        :number: TODO
        :returns: TODO

        """
        next_num = None
        for item in range(0, 101):
            usable, number = self._reduce_to_zero(number + item)
            if usable:
                next_num = item
                break

        return next_num

    def _look_negative(self, number):
        """TODO: Docstring for _look_negative.

        :number: TODO
        :returns: TODO

        """
        next_num = None
        for item in range(-100, 0):
            usable, number = self._reduce_to_zero(number + item)
            if usable:
                next_num = item
                break

        return next_num

    def _find_triplet(self, start, positives):
        """Select the best next number of the triplet
        :returns: int, the number which is also the key of the self.tree dict

        """
        triplet = None

        if positives:
            number = self._look_positive(start)
            if number is None:
                number = self._look_negative(start)
                if number is not None:
                    triplet = self._remove_numbers(start,
                                                   number,
                                                   start + number)
            else:
                triplet = self._remove_numbers(start, number, start + number)
        else:
            number = self._look_positive(start)
            if number is None:
                number = self._look_negative(start)
                if number is not None:
                    triplet = self._remove_numbers(start,
                                                   number,
                                                   start + number)

            else:
                triplet = self._remove_numbers(start, number, start + number)

        if triplet is not None:
            self.triplets.append(triplet)

    def _reduce_to_zero(self, pair_sum):
        """Find if there's the inverse of the first 2 numbers

            if sum = 98 then look for -98
            if sum = -98 then look for 98

        :self.tree: dict, Dictionary with all the numbers
        :pair_sum: int, the sum of the first 2 numbers
        :returns: Bool, True if the inverse exists, False otherwise

        """
        if (pair_sum * -1) in self.tree and self.tree[pair_sum * -1] > 0:
            return (True, (pair_sum * -1))
        return (False, -101)

    def _remove_numbers(self, first, second, third):
        """Remove the triplet from the dictionary

        TODO: Should we use a vector instead ?

        :self.tree: dict, Dictionary with all the numbers
        :first: int, the first number of the triplet
        :second: int, the first number of the triplet
        :third: int, the first number of the triplet
        :returns: dict, the self.tree with decreased index if the found triplet

        """
        result = min_element(
            {
                first: self.tree[first],
                second: self.tree[second],
                third: self.tree[third],
            }
        )

        self.tree[first] -= result[1]
        self.tree[second] -= result[1]
        self.tree[third] -= result[1]

        return Triplet([first, second, third], result[1])

    def log_triplets(self):
        """TODO: Docstring for log_triplet.
        :returns: TODO

        """
        with open(self.output, "w") as data:
            data.write("Triplets\t\t\tAmount")
            for item in self.triplets:
                data.write(item + "\n")
            data.write("\nTime: {0}")

    def start(self):
        """Look for the next triplet of numbers
        :returns: Tuple, Returns a tuple with a vector of the 3 numbers and the
                         updated dictionary, And empty vector is return if no
                         triplet was found
        """

        for number in range(-100, 101):
            if number in self.tree:
                usable = True
                sign = True if number >= 0 else False
                while usable or self.tree[number] > 0:
                    usable = self._find_triplet(number, sign)
            pass
        pass


if __name__ == "__main__":
    raise Exception(
        "This script is not intended to be used as a standalone script")
