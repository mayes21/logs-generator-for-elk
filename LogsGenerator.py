#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import logging
import random
from time import sleep


def __generate_logs():
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


def main():
    # argument parser
    parser = argparse.ArgumentParser(description="Logs generator for ELK stack")
    parser.add_argument("-p", help="Logs path")
    args = parser.parse_args()
    # logging configuration
    logging.basicConfig(level=logging.DEBUG,
                        filemode='a',
                        format='%(asctime)s %(levelname)s : %(message)s',
                        datefmt='%d-%m-%Y %H:%M:%S')
    if args.p is not None:
        print("Start generation of logs")
        while True:
            __generate_logs()


if __name__ == '__main__':
    main()

