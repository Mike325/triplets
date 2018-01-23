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

# debug_mode = False


def status_msg(message):
    """Print status message

    :message: TODO
    :returns: TODO

    """
    print("[*]  {0}".format(message))


def verbose_msg(message):
    """TODO: Docstring for verbose_msg.

    :message: TODO
    :returns: TODO

    """
    global debug_mode
    if debug_mode is True:
        print("[!]  ---- Debug: {0}".format(message))


def warning_msg(message):
    """TODO: Docstring for status_message.

    :message: TODO
    :returns: TODO

    """
    print("[!]  ---- Warning: {0}".format(message))


def error_msg(message):
    """TODO: Docstring for status_message.

    :message: TODO
    :returns: TODO

    """
    print("[X]  ---- Error: {0}".format(message))


if __name__ == "__main__":
    raise Exception("This script is intended to be used as a module")
