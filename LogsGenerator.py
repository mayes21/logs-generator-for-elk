#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import argparse
import sys
import logging
import random
# from logstash_async.handler import AsynchronousLogstashHandler
# from logstash_async.handler import LogstashFormatter
import logstash
from time import sleep

host = "logstash"
port = 5000


def __generate_logs(logger):
    x = random.randint(0, 4)
    sleep(1)
    if x == 0:
        logger.warning('Logging WARNING Message')
    elif x == 1:
        logger.critical('Logging CRITICAL Message')
    elif x == 2:
        logger.info('Logging INFO Message')
    elif x == 3:
        logger.debug('Logging DEBUG Message')
    else:
        logger.error('Logging ERROR Message')


def main():
    # argument parser
    # parser = argparse.ArgumentParser(description="Logs generator for ELK stack")
    # parser.add_argument("-p", help="Logs path")
    # args = parser.parse_args()
    # logging configuration
    # logging.basicConfig(level=logging.DEBUG,
    #                     filemode='a',
    #                     format='%(asctime)s %(levelname)s : %(message)s',
    #                     datefmt='%d-%m-%Y %H:%M:%S')

    logger = logging.getLogger("python-logstash-logger")
    logger.setLevel(logging.DEBUG)

    logger.addHandler(logstash.TCPLogstashHandler(host, port))  # default port : 5959

    # handler = AsynchronousLogstashHandler(
    #     host=host,
    #     port=port,
    #     ssl_enable=False,
    #     ssl_verify=False,
    #     database_path=''
    # )

    # formatter = LogstashFormatter()
    # logger.setFormatter(formatter)
    #
    # logger.addHandler(handler)

    # if args.p is not None:
    print("Start generation of logs")
    while True:
        try:
            __generate_logs(logger)
        except KeyboardInterrupt:
            logging.fatal('KEYBOARD INTERRUPT')
            sys.exit(0)


if __name__ == '__main__':
    main()

