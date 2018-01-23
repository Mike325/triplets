#!/usr/bin/env python3

from files.genfiles import checkFiles
from files.genfiles import getArray
from algorithm.triplet import TripletMaker
from logger.logger import status_msg
# from logger.logger import error_msg
# from logger.logger import verbose_msg
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
debug_mode = False
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
    parser.add_argument("-o",
                        "--output",
                        help="Output file with the Triplets",
                        required=False,
                        metavar='LOG',
                        default="triplets.log",
                        dest="output",
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
    parser.add_argument("--version",
                        help="Shows the version",
                        required=False,
                        dest="version",
                        action="store_true")

    cli_args = parser.parse_args()

    return cli_args


def main():
    """Main function
    """
    global debug_mode
    global start_time

    cli_args = __parse_arguments()

    if cli_args.version:
        status_msg("Current version {0}".format(__version__))
        return 0

    debug_mode = cli_args.verbose

    start_time = time.time()
    checkFiles(cli_args.override)

    for item in [1000, 2000, 5000, 10000, 100000, 1000000]:
        array = getArray(item)
        maker = TripletMaker(array, cli_args.output)
        maker.start()

    final_time = str(time.time() - start_time)
    status_msg("Final time {0}".format(final_time))


if __name__ == "__main__":
    main()
else:
    raise Exception(
        "This script is not intended to be used as a module")
