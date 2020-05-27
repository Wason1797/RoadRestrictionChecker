from utils.parser import to_time


class RuleSetTemplate:

    WEEK_DAY_RESTRICTIONS = {
        1: {1, 2},
        2: {3, 4},
        3: {5, 6},
        4: {7, 8},
        5: {9, 0},
        6: {},
        7: {},
    }

    ALLOW_SPECIAL_CASES = True


class GeneralRuleset(RuleSetTemplate):

    TIME_WINDOWS = ((to_time('7:00'), to_time('9:30')),
                    (to_time('16:00'), to_time('19:30')))


class ExtendedRuleset(RuleSetTemplate):

    TIME_WINDOWS = ((to_time('5:00'), to_time('20:00')), )


class LockdownRuleset(RuleSetTemplate):

    WEEK_DAY_RESTRICTIONS = {week_day: {1, 2, 3, 4, 5, 6, 7, 8, 9, 0} - digits
                             for week_day, digits in super().WEEK_DAY_RESTRICTIONS.items()}

    TIME_WINDOWS = ((to_time('14:00'), to_time('5:00')), )
