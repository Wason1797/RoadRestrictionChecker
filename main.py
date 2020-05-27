from utils import parser
from models.plate import Plate
from checker import RoadRestrictionChecker
from config.restrictions import GeneralRuleset


if __name__ == "__main__":
    args = parser.configure_argument_parser().parse_args()
    time = parser.to_time(args.time)
    week_day = parser.to_date(args.date).isoweekday()
    plate = Plate(args.plate)

    if RoadRestrictionChecker(GeneralRuleset).is_car_restricted(plate, week_day, time):
        print("You have road restriction at the moment")
    else:
        print("You don't have road restriction at the moment")
