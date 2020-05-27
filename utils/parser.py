from datetime import datetime, date
from errors.validation_errors import InputValidationError

import time


def to_time(time_input: str, _format: str = r'%H:%M') -> time.struct_time:
    try:
        return time.strptime(time_input, _format)
    except ValueError:
        raise InputValidationError(f"{time_input} is not a valid time string with format: {_format}")


def to_date(date_input: str, _format: str = None) -> datetime:
    try:
        return datetime.strptime(date_input, _format) if _format else date.fromisoformat(date_input)
    except ValueError:
        raise InputValidationError(f"{date_input} is not a valid date with format {_format or 'ISO format'}")
