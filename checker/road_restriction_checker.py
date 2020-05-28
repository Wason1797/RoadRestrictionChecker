from models.plate import Plate
from config.restrictions import RuleSet


class RoadRestrictionChecker:

    def __init__(self, rule_set: RuleSet):
        self.rule_set = rule_set

    def is_plate_restricted(self, plate: Plate, week_day: int) -> bool:
        return plate.last_digit in self.rule_set.WEEK_DAY_RESTRICTIONS.get(week_day)

    def is_time_restricted(self, time) -> bool:
        return any(time > lower_bound and time < upper_bound for lower_bound, upper_bound in self.rule_set.TIME_WINDOWS)

    def is_special_case(self, plate: Plate):
        return plate.plate_type not in self.rule_set.APPLY_TO

    def is_car_restricted(self, plate: Plate, week_day: int, time) -> bool:
        print(f"{plate} belongs to a {plate.plate_type}")
        print(f"Current config applies to {', '.join(self.rule_set.APPLY_TO)}")

        return False if self.is_special_case(plate) else True \
            if self.is_plate_restricted(plate, week_day) and self.is_time_restricted(time) else False
