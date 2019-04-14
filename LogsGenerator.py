#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import random
from time import sleep

logging.basicConfig(filename="logFile.log",
                    level=logging.DEBUG,
                    filemode='a',
                    format='%(asctime)s %(levelname)s : %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S')


def main():
    print("Start generation of logs")
    while True:
        x = random.randint(0, 4)
        sleep(1)
        if x == 0:
            logging.warning('Logging WARNING Message')
        elif x == 1:
            logging.critical('Logging CRITICAL Message')
        elif x == 2:
            logging.info('Logging INFO Message')
        elif x == 3:
            logging.debug('Logging DEBUG Message')
        else:
            logging.error('Logging ERROR Message')


if __name__ == '__main__':
    main()

