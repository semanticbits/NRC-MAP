"""Validations

This file provides the support of basic validations for unit tests

"""
import pandas as pd


def validate_csv(filename, header, cols, rows):
    """
    Validates a files data using the provided parameters

    :param filename: File and path to be validated
    :param header: String header expected to be on file
    :param cols: Integer number of columns expected in file
    :param rows: Integer number of rows expected in file
    """

    # open file
    data = pd.read_csv(filename, delimiter='|')

    # validate header
    header_result = header == '|'.join(list(data.columns.values))

    # validate column count
    column_result = data.shape[1] == cols

    # validate row count
    row_result = data.shape[0] == rows

    return (header_result == column_result == row_result) is True
