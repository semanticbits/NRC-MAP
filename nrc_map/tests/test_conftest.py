#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" pytest Fixtures Unit Tests

"""
import datetime

from .conftest import TEST_TIME


def test_patch_datetime(patch_datetime):
    assert datetime.datetime.now() == TEST_TIME
