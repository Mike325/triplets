#!/usr/bin/env python3

from files.genfiles import check_files
from files.genfiles import get_array
from files.genfiles import log_triplets
from files.genfiles import get_filename
from algorithm.triplet import TripletMaker
from logger.messages import status
from logger.messages import error
from logger.messages import verbose
from logger import messages
import argparse
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

__version__ = "0.1.0"
start_time = None


def __parse_arguments():
    """ Function to parse CLI args
    :returns: object with the CLI arguments

    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-s",
                        "--seed",
                        help="Seed for the random numbers",
                        metavar='SEED',
                        required=False,
                        dest="seed",
                        type=int)
    parser.add_argument("-t",
                        "--test",
                        help="Type of test to run, ALL, 100 or 1M",
                        required=False,
                        default="1M",
                        metavar='TEST',
                        dest="test",
                        type=str)
    parser.add_argument("--override",
                        help="Force file creation",
                        required=False,
                        dest="override",
                        action="store_true")
    parser.add_argument("-v",
                        "--verbose",
                        help="Enable debug messages",
                        required=False,
                        dest="verbose",
                        action="store_true")
    parser.add_argument("-l",
                        "--logger",
                        help="Enable logger",
                        required=False,
                        dest="logger",
                        action="store_true")
    parser.add_argument("-q",
                        "--quiet",
                        help="Silence all stout output",
                        required=False,
                        dest="quiet",
                        action="store_true")
    parser.add_argument("--version",
                        help="Shows the version",
                        required=False,
                        dest="version",
                        action="store_true")

    cli_args = parser.parse_args()

    return cli_args


def _multi_length(override=False):
    """TODO: Docstring for _multi_length.
    :returns: TODO

    """

    for item in [1000, 2000, 5000, 10000, 100000, 1000000]:
        check_files(size=item, override=override)
        array = get_array(size=item)
        maker = TripletMaker(array)
        maker.start()
        log_triplets(maker.size, maker.triplets, maker.time)


def _same_size_length(override=False):
    """TODO: Docstring for _same_size_length.

    :override: TODO
    :output: TODO
    :returns: TODO

    """

    for item in range(0, 100):
        filename = get_filename(100000)
        check_files(size=100000, filename="{0}_{1}.txt".format(item, filename))
        array = get_array(filename="{0}_{1}.txt".format(item, filename))
        maker = TripletMaker(array)
        maker.start()
        log_triplets(size=maker.size,
                     triplets=maker.triplets,
                     searchtime=maker.time,
                     filename="{0}_{1}.log".format(item, filename))


def main():
    """Main function
    """
    global debug_mode
    global start_time

    cli_args = __parse_arguments()

    if cli_args.version:
        status("Current version {0}".format(__version__))
        return 0

    messages.debug_mode = cli_args.verbose
    messages.quiet = cli_args.quiet
    messages.logger = cli_args.logger

    start_time = time.time()

    if cli_args.test == "1M" or cli_args.test == "all":
        _multi_length(cli_args.override)

    if cli_args.test == "100" or cli_args.test == "all":
        _same_size_length(cli_args.override)

    final_time = str(time.time() - start_time)
    status("Final time {0}".format(final_time))


if __name__ == "__main__":
    main()
else:
    raise Exception(
        "This script is not intended to be used as a module")
