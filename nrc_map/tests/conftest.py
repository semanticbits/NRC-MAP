#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Test Configuration File

"""
import datetime

import pytest


TEST_TIME = datetime.datetime(2019, 12, 25, 8, 16, 32)


@pytest.fixture
def patch_datetime(monkeypatch):

    class CustomDatetime:
        @classmethod
        def now(cls):
            return TEST_TIME

    monkeypatch.setattr(datetime, 'datetime', CustomDatetime)
