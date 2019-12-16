#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Command Line Interface Module

"""
import logging
import time

import click


@click.command()
@click.argument('number')
@click.option('-q', '--quiet', is_flag=True, multiple=True,
              help='Decrease output level one (-q) or multiple times (-qqq).')
@click.option('-v', '--verbose', is_flag=True, multiple=True,
              help='Increase output level one (-v) or multiple times (-vvv).')
def count(number: int, quiet, verbose):
    """
    Display progressbar while counting to the user provided integer `number`.

    ..note:: This is an example to follow when creating new commandline
        functions.
    """
    click.clear()
    logging_level = logging.INFO + 10 * len(quiet) - 10 * len(verbose)
    logging.basicConfig(level=logging_level)
    with click.progressbar(range(int(number)), label='Counting') as bar:
        for n in bar:
            click.secho(f'\n\nProcessing: {n}', fg='green')
            time.sleep(0.1)


if __name__ == '__main__':
    pass
