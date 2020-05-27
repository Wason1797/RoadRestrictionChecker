import re


class Plate:

    valid_regex: str = r"(^[a-zA-Z]{2,3}-?[0-9]{3,4}$|^[a-zA-Z]{2}-?[0-9]{3}[a-zA-Z]$)"
    special_cases: dict = {
        'E': 'Goverment Vehicle',
        'X': 'Official Vehicle',
        'M': 'GAD Vehicle',
        'A': 'Comercial Vehicle',
        'U': 'Comercial Vehicle',
        'Z': 'Comercial Vehicle',
    }

    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return self.value

    @property
    def is_valid(self) -> bool:
        return bool(re.match(self.valid_regex, self.value))
