from models.plate import Plate
from utils.constants import VehicleTypes

import pytest

VALID_PLATE_INPUTS = (
    'XXX-001',
    'Xxx-0004',
    'XXx000',
    'AXX0005',
    'XX009x',
)


@pytest.mark.parametrize("plate_input", VALID_PLATE_INPUTS)
def test_valid_plate_init(plate_input):
    plate = Plate(plate_input)
    assert plate.value == plate_input


@pytest.mark.parametrize("plate_input", [
    'XX#-000',
    'XXX--0000',
    'XX+00',
    'xxx',
    'XB0006',
    ''
])
def test_invalid_plate_init(plate_input):
    with pytest.raises(ValueError) as excinfo:
        Plate(plate_input)
    assert 'PlateValidationError' == excinfo.typename


@pytest.mark.parametrize("plate_input,expected_digit", zip(
    VALID_PLATE_INPUTS, (1, 4, 0, 5, 9)
))
def test_get_last_digit(plate_input, expected_digit):
    assert Plate(plate_input).last_digit == expected_digit


@pytest.mark.parametrize("plate_input,expected_code", zip(
    VALID_PLATE_INPUTS, ('XXX', 'Xxx', 'XXx', 'AXX', 'XX')
))
def test_get_letter_code(plate_input, expected_code):
    assert Plate(plate_input).letter_code == expected_code


@pytest.mark.parametrize("plate_input,expected_type", [
    ('AT-0012', VehicleTypes.AT_VEHICLE),
    ('CC-0012', VehicleTypes.CC_VEHICLE),
    ('CD-0012', VehicleTypes.CD_VEHICLE),
    ('XAC-0012', VehicleTypes.COMERCIAL_VEHICLE),
    ('XUC-0012', VehicleTypes.COMERCIAL_VEHICLE),
    ('XZC-0012', VehicleTypes.COMERCIAL_VEHICLE),
    ('AMC-0012', VehicleTypes.GAD_VEHICLE),
    ('PEB-0001', VehicleTypes.GOV_VEHICLE),
    ('IT-0012', VehicleTypes.IT_VEHICLE),
    ('GXA-0100', VehicleTypes.OFFICIAL_VEHICLE),
    ('OI-0012', VehicleTypes.OI_VEHICLE),
    ('EBA-0234', VehicleTypes.PRIVATE_VEHICLE),
])
def test_get_plate_type(plate_input, expected_type):
    assert Plate(plate_input).plate_type == expected_type
