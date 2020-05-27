from models.plate import Plate
from utils.parser import to_date, to_time
from checker import RoadRestrictionChecker
from config.restrictions import GeneralRuleset, ExtendedRuleset, LockdownRuleset

import pytest


@pytest.mark.parametrize("plate_input,date_input,ruleset,expected_output", [
    ('AAC-0875', '2020-05-27', GeneralRuleset, True),
    ('AAC-0875', '2020-05-20', ExtendedRuleset, True),
    ('AAC-0875', '2020-05-28', LockdownRuleset, True),
    ('AAC-0875', '2020-05-25', GeneralRuleset, False),
    ('AAC-0875', '2020-05-26', ExtendedRuleset, False),
    ('AAC-0875', '2020-05-27', LockdownRuleset, False),
    ('AXC-0875', '2020-05-27', LockdownRuleset, False),
])
def test_is_plate_restricted(plate_input, date_input, ruleset, expected_output):
    assert RoadRestrictionChecker(ruleset).is_plate_restricted(Plate(plate_input),
                                                               to_date(date_input).isoweekday()) == expected_output


@pytest.mark.parametrize("time_input,ruleset,expected_output", [
    ('17:30', GeneralRuleset, True),
    ('7:00', GeneralRuleset, False),
    ('9:31', ExtendedRuleset, True),
    ('1:00', LockdownRuleset, True),
    ('13:00', GeneralRuleset, False),
    ('22:00', ExtendedRuleset, False),
    ('13:00', LockdownRuleset, False),
    ('6:00', LockdownRuleset, False),
])
def test_is_time_restricted(time_input, ruleset, expected_output):
    assert RoadRestrictionChecker(ruleset).is_time_restricted(to_time(time_input)) == expected_output


@pytest.mark.parametrize("plate_input,ruleset,expected_output", [
    ('AXC-0875', GeneralRuleset, True),
    ('LMA-0010', ExtendedRuleset, True),
    ('GXA-0100', LockdownRuleset, True),
    ('AAB-0123', GeneralRuleset, False),
    ('AUB-0123', ExtendedRuleset, False),
    ('AAC-0875', LockdownRuleset, False),
])
def test_is_special_case(plate_input, ruleset, expected_output):
    assert RoadRestrictionChecker(ruleset).is_special_case(Plate(plate_input)) == expected_output


@pytest.mark.parametrize("plate_input,date_input,time_input,ruleset,expected_output", [
    ('AAC-0875', '2020-05-27', '17:30', GeneralRuleset, True),
    ('AAC-0875', '2020-05-20', '9:31', ExtendedRuleset, True),
    ('AAC-0875', '2020-05-28', '1:00', LockdownRuleset, True),
    ('AAC-0876', '2020-05-27', '13:00', GeneralRuleset, False),
    ('AAC-0876', '2020-05-20', '22:00', ExtendedRuleset, False),
    ('AAC-0876', '2020-05-28', '13:00', LockdownRuleset, False),
])
def test_is_car_restricted(plate_input, date_input, time_input, ruleset, expected_output):
    assert RoadRestrictionChecker(ruleset).is_car_restricted(Plate(plate_input),
                                                             to_date(date_input).isoweekday(),
                                                             to_time(time_input)) == expected_output
