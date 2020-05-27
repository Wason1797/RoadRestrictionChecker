from datetime import date
import time


if __name__ == "__main__":
    plate = 'EBA-0238'
    date_str = '2019-08-15'
    time_of_day = time.strptime('17:05', r'%H:%M')
    time_windows = ((time.strptime('7:00', r'%H:%M'), time.strptime('9:30', r'%H:%M')),
                    (time.strptime('16:00', r'%H:%M'), time.strptime('19:30', r'%H:%M')))
    week_days = (1, 2, 3, 4, 5, 6, 7)
    plate_digits = ({1, 2}, {3, 4}, {5, 6}, {7, 8}, {9, 0}, {}, {})

    restrictions = dict(zip(week_days, plate_digits))
    week_day = date.fromisoformat(date_str).isoweekday()

    print(week_day)
    if int(plate[-1]) in restrictions.get(week_day, {}) \
            and all(time_of_day >= lower_window or time_of_day <= upper_window for lower_window, upper_window in time_windows):
        print("Do not circulate")
    else:
        print("allowed")
