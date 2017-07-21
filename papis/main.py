#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import logging


logger = logging.getLogger("papis")
if "--debug" in sys.argv:
    log_format = '%(relativeCreated)d-'
    log_format += '%(levelname)s:%(name)s:%(message)s'
    logging.basicConfig(level=logging.DEBUG, format=log_format)
    sys.argv.pop(sys.argv.index("--debug"))
    logger.debug("DEBUG MODE FOR DEVELOPERS ON")


import papis.commands


def main():
    papis.commands.init()
    papis.commands.main()


if sys.version_info < (3, 2):
    raise Exception("This script must use python 3.2 or greater")

if __name__ == "__main__":
    main()

# vim:set et sw=4 ts=4 ft=python:
