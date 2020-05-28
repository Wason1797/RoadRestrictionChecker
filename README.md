# RoadRestrictionChecker

A little program that tells you when your car is allowed on the road

The tables below show the restrictions implemented and tested in the code.

**Standard Rules**

|   Weekday    | Digits  |          Time of day           |
|--------------|:-------:|--------------------------------|
| 1 (Monday)   |  1, 2   |(7:00 to 9:30), (16:00 to 19:30)|
| 2 (Tuesday)  |  3, 4   |(7:00 to 9:30), (16:00 to 19:30)|
| 3 (Wednesday)|  5, 6   |(7:00 to 9:30), (16:00 to 19:30)|
| 4 (Thursday) |  7, 8   |(7:00 to 9:30), (16:00 to 19:30)|
| 5 (Friday)   |  9, 0   |(7:00 to 9:30), (16:00 to 19:30)|
| 6 (Saturday) |         |                                |
| 7 (Sunday)   |         |                                |

**Extended Rules**

|   Weekday    | Digits  |  Time of day  |
|--------------|:-------:|---------------|
| 1 (Monday)   |  1, 2   |(5:00 to 20:00)|
| 2 (Tuesday)  |  3, 4   |(5:00 to 20:00)|
| 3 (Wednesday)|  5, 6   |(5:00 to 20:00)|
| 4 (Thursday) |  7, 8   |(5:00 to 20:00)|
| 5 (Friday)   |  9, 0   |(5:00 to 20:00)|
| 6 (Saturday) |         |               |
| 7 (Sunday)   |         |               |

**Lockdown Rules**

|   Weekday    |          Digits            |           Time of day          |
|--------------|:--------------------------:|--------------------------------|
| 1 (Monday)   |3, 4, 5, 6, 7, 8, 9, 0      |(0:00 to 5:00), (14:00 to 23:59)|
| 2 (Tuesday)  |1, 2, 5, 6, 7, 8, 9, 0      |(0:00 to 5:00), (14:00 to 23:59)|
| 3 (Wednesday)|1, 2, 3, 4, 7, 8, 9, 0      |(0:00 to 5:00), (14:00 to 23:59)|
| 4 (Thursday) |1, 2, 3, 4, 5, 6, 9, 0      |(0:00 to 5:00), (14:00 to 23:59)|
| 5 (Friday)   |1, 2, 3, 4, 5, 6, 7, 8      |(0:00 to 5:00), (14:00 to 23:59)|
| 6 (Saturday) |1, 2, 3, 4, 5, 6, 7, 8, 9, 0|(0:00 to 5:00), (14:00 to 23:59)|
| 7 (Sunday)   |1, 2, 3, 4, 5, 6, 7, 8, 9, 0|(0:00 to 5:00), (14:00 to 23:59)|

Nevertheless as per request, only the standard rules apply by default. You can change or implement your own rulesets following this blueprint:

```python
class PersonalizedRuleset(RuleSet):

    # A dictionary that notates the isoweekday and a set of digits that need to follow the restrction
    WEEK_DAY_RESTRICTIONS = {
        1: {1, 2},
        2: {3, 4},
        3: {5, 6},
        4: {7, 8},
        5: {9, 0},
        6: set(),
        7: set(),
    }
    # Set with the vehicle types that need to follow the ruleset
    APPLY_TO = {VehicleTypes.COMERCIAL_VEHICLE,
                VehicleTypes.PRIVATE_VEHICLE}

    # Add as many time windows during the day when the restriction applies
    TIME_WINDOWS = ((to_time('7:00'), to_time('9:30')),
                    (to_time('16:00'), to_time('19:30')))
```

This program uses python 3.7.5 and pytest for unit testing.
To run the program you issue the following command:

```bash
python main.py -time 8:30 -date 2020-05-27 -plate ABC-875
```

Please use valid formats for the input: _(HH:MM, yyy-mm-dd, XXX-####)_

To run all the test cases you need to install pytest with:

```bash
pip install pytest
```

And run

```bash
pytest -v
```

Note: All the commands should be run in the root workspace folder.
