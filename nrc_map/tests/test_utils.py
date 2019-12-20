#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Utilities Unit Tests

"""
from pathlib import Path
import logging
import os
import warnings

import pytest

from .. import exceptions
from .. import utils


LOGGER = logging.getLogger(__name__)

# Test logger_setup()
logger_setup = {
    'default args': (None, Path('info.log')),
    'file_path': ('test_p', Path('test_p_2019-12-25_08:16:32.log')),
}


@pytest.mark.parametrize('file_path, log_file',
                         list(logger_setup.values()),
                         ids=list(logger_setup.keys()))
def test_logger_setup(patch_datetime, file_path, log_file):
    logger = utils.logger_setup(file_path)
    assert isinstance(logger, logging.Logger)
    assert log_file in list(Path().glob('*.log'))
    log_file.unlink()


# Test nested_get()
nested_get = {
    'first level': (['x'], 0),
    'nested level': (['a', 'b', 'c'], 2),
}


@pytest.mark.parametrize('key_path, expected',
                         list(nested_get.values()),
                         ids=list(nested_get.keys()))
def test_nested_get(key_path, expected):
    sample_dict = {'a': {'b': {'c': 2}, 'y': 1}, 'x': 0}
    assert utils.nested_get(sample_dict, key_path) == expected


# Test nested_set()
nested_set = {
    'first level': (['x'], 00),
    'nested level': (['a', 'b', 'c'], 22),
}


@pytest.mark.parametrize('key_path, value',
                         list(nested_set.values()),
                         ids=list(nested_set.keys()))
def test_nested_set(key_path, value):
    sample_dict = {'a': {'b': {'c': 2}, 'y': 1}, 'x': 0}
    utils.nested_set(sample_dict, key_path, value)
    assert utils.nested_get(sample_dict, key_path) == value


# Test progress_str()
progress_str = {
    '0%': (0, 100, '\rProgress:  0.0%'),
    '100%': (100, 100, '\rProgress:  100.0%\n\n'),
}


@pytest.mark.parametrize('n, total, expected',
                         list(progress_str.values()),
                         ids=list(progress_str.keys()))
def test_progress_str(n, total, expected):
    assert utils.progress_str(n, total) == expected


def test_progress_str_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        utils.progress_str(100, 0)


def test_progress_str_input_error():
    with pytest.raises(exceptions.InputError):
        utils.progress_str(100, 50)


# Test project_vars():
def test_project_vars():
    utils.project_vars()
    assert os.environ['ACCEPT_EULA'] == 'Y'


# Test status():
def test_status(caplog):

    @utils.status(LOGGER)
    def foo():
        return 5

    foo()
    assert 'Initiated: foo' in caplog.text


# Test warning_format()
def test_warning_format(patch_datetime):
    utils.warning_format()
    with pytest.warns(UserWarning):
        warnings.warn('test', UserWarning)
