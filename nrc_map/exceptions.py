#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Exception Module

"""


class Error(Exception):
    """Base class for package exceptions.

    :Attributes:

    - **expression**: *str* input expression in which the error occurred
    - **message**: *str* explanation of the error
    """

    def __init__(self, expression: str, message: str):
        self.expression = expression
        self.message = message


class InputError(Error):
    """Exception raised for errors in the input."""
