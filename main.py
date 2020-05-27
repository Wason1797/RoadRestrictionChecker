from utils import parser
from models.plate import Plate
from checker import RoadRestrictionChecker
from config.restrictions import GeneralRuleset as ruleset
from errors.validation_errors import PlateValidationError


if __name__ == "__main__":
    args = parser.configure_argument_parser().parse_args()
    time = parser.to_time(args.time)
    week_day = parser.to_date(args.date).isoweekday()
    plate = Plate(args.plate)

    if not plate.is_valid:
        raise PlateValidationError(f"Plate {plate} does not match the allowed standard")

    print(f"{plate} belongs to a {plate.plate_type}")
    print(f"Current config {'allows' if ruleset.ALLOW_SPECIAL_CASES else 'dont allow'} special cases")

    if RoadRestrictionChecker(ruleset).is_car_restricted(plate, week_day, time):
        print(f"You have road restriction at the moment")
    else:
        print("You don't have road restriction at the moment")
