from datetime import datetime
from argparse import ArgumentParser
from errors.validation_errors import InputValidationError

import time


def to_time(time_input: str, _format: str = r'%H:%M') -> time.struct_time:
    try:
        return time.strptime(time_input, _format)
    except ValueError:
        raise InputValidationError(f"{time_input} is not a valid time string with format: {_format}")


def to_date(date_input: str, _format: str = None) -> datetime:
    try:
        return datetime.strptime(date_input, _format) if _format else datetime.fromisoformat(date_input)
    except ValueError:
        raise InputValidationError(f"{date_input} is not a valid date with format: {_format or 'ISO format'}")


def configure_argument_parser() -> ArgumentParser:
    parser = ArgumentParser(description="Road Restriction Checker, be aware when you are allowed to be on the road ...")
    parser.add_argument('-plate', help="Enter a valid car plate i.e. (XXX-### XX-###X)", type=str, required=True)
    parser.add_argument('-date', help="Enter a date following this format yyyy-mm-dd", type=str, required=True)
    parser.add_argument('-time', help="Enter a 24 hour time following this format hh:mm", type=str, required=True)
    return parser
