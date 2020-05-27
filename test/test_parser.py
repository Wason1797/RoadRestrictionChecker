from utils import parser
from time import struct_time
from datetime import datetime
from argparse import ArgumentParser

import pytest


@pytest.mark.parametrize("time_input,expected_time", [
    ('00:00', (0, 0)),
    ('01:10', (1, 10)),
    ('20:17', (20, 17)),
    ('23:59', (23, 59)),
])
def test_to_time_with_valid_input(time_input, expected_time):
    expected_hour, expected_minute = expected_time
    time_output = parser.to_time(time_input)
    assert isinstance(time_output, struct_time)
    assert time_output.tm_hour == expected_hour
    assert time_output.tm_min == expected_minute


@pytest.mark.parametrize("time_input", [
    '00:70',
    '25:10',
    '20;17',
    'AAAA',
])
def test_to_time_with_invalid_input(time_input):
    with pytest.raises(ValueError, match=f"{time_input} .*") as excinfo:
        parser.to_time(time_input)
    assert 'InputValidationError' == excinfo.typename


@pytest.mark.parametrize("date_input,expected_date", [
    ('2020-08-17', (2020, 8, 17)),
    ('1999-01-30', (1999, 1, 30)),
    ('2050-06-28', (2050, 6, 28)),
    ('2001-09-12', (2001, 9, 12)),
])
def test_to_date_with_valid_input(date_input, expected_date):
    expected_year, expected_month, expected_day = expected_date
    date_output = parser.to_date(date_input)
    assert isinstance(date_output, datetime)
    assert date_output.year == expected_year
    assert date_output.month == expected_month
    assert date_output.day == expected_day


@pytest.mark.parametrize("date_input", [
    '00:70',
    '4040-44-20',
    '2020-02-31',
    '2000_09_08',
])
def test_to_date_with_invalid_input(date_input):
    with pytest.raises(ValueError, match=f"{date_input} .*") as excinfo:
        parser.to_date(date_input)
    assert 'InputValidationError' == excinfo.typename


def test_configure_argument_parser():
    cmd_parser = parser.configure_argument_parser()
    assert isinstance(cmd_parser, ArgumentParser)
