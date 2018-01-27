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

debug_mode = False


def status(message):
    """Print status message

    :message: TODO
    :returns: TODO

    """
    with open("messages.log", "a") as messages:
        print("[*]  {0}".format(message))
        messages.write("[*]  {0}\n".format(message))


def verbose(message):
    """TODO: Docstring for verbose.

    :message: TODO
    :returns: TODO

    """
    global debug_mode
    if debug_mode is True:
        with open("messages.log", "a") as messages:
            print("[!]  ---- Debug: {0}".format(message))
            messages.write("[!]  ---- Debug: {0}\n".format(message))


def warning(message):
    """TODO: Docstring for status_message.

    :message: TODO
    :returns: TODO

    """
    with open("messages.log", "a") as messages:
        print("[!]  ---- Warning: {0}".format(message))
        messages.write("[!]  ---- Warning: {0}\n".format(message))


def error(message):
    """TODO: Docstring for status_message.

    :message: TODO
    :returns: TODO

    """
    with open("messages.log", "a") as messages:
        print("[X]  ---- Error: {0}".format(message))
        messages.write("[X]  ---- Error: {0}".format(message))


if __name__ == "__main__":
    raise Exception("This script is intended to be used as a module")
