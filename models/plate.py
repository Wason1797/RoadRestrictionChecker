from utils.constants import VehicleTypes
from errors.validation_errors import PlateValidationError

import re


class Plate:

    valid_regex: str = r"(^([a-zA-Z]{3}|[cCoOdDiIaAtT]{2})-?[0-9]{3,4}$|^[a-zA-Z]{2}-?[0-9]{3}[a-zA-Z]$)"
    letter_code_regex: str = r"^[a-zA-Z]{2,3}"

    special_gov_cases: dict = {
        'E': VehicleTypes.GOV_VEHICLE,
        'X': VehicleTypes.OFFICIAL_VEHICLE,
        'M': VehicleTypes.GAD_VEHICLE,
        'A': VehicleTypes.COMERCIAL_VEHICLE,
        'U': VehicleTypes.COMERCIAL_VEHICLE,
        'Z': VehicleTypes.COMERCIAL_VEHICLE,
    }

    special_international_cases: dict = {
        'CC': VehicleTypes.CC_VEHICLE,
        'CD': VehicleTypes.CD_VEHICLE,
        'OI': VehicleTypes.OI_VEHICLE,
        'AT': VehicleTypes.AT_VEHICLE,
        'IT': VehicleTypes.IT_VEHICLE,
    }

    def __init__(self, value: str):
        if re.match(self.valid_regex, value):
            self.value = value
        else:
            raise PlateValidationError(f"Plate {value} does not match the allowed standard")

    def __repr__(self):
        return self.value

    @property
    def last_digit(self) -> int:
        return int(self.value[-1] if str.isdigit(self.value[-1]) else self.value[-2])

    @property
    def letter_code(self) -> str:
        return re.search(self.letter_code_regex, self.value).group(0)

    @property
    def plate_type(self) -> str:
        gov_type = self.special_gov_cases.get(self.value[1].upper())
        international_type = self.special_international_cases.get(self.letter_code.upper())
        return gov_type if gov_type else international_type if international_type else VehicleTypes.PRIVATE_VEHICLE
