def get_persons_time(intervals: dict) -> list:
    """
        return sorted list[tuple]:
        (1, 1),
        (2, -1),
        (3, 1),
        ...

        weight tuple[1]:
        1 - odd,
        -1 - even
    """
    time_with_weight = []

    for val in intervals.values():
        for idx in range(len(val)):
            if idx % 2 == 0 and val[idx] <= intervals['lesson'][1]:
                time_with_weight.append((val[idx], 1))
            elif idx % 2 != 0 and val[idx] <= intervals['lesson'][1]:
                time_with_weight.append((val[idx], -1))
    
    return sorted(time_with_weight)


def get_total_interval_time(intervals: dict) -> list:
    """
        returns start and end time when pupil and tutor were connected - list[tuple]

        the joint time starts when the weight is 3
    """
    appearence_start_and_end_time = []
    current_weight = 0
    next_weight = 0

    for time in get_persons_time(intervals):
        next_weight += time[1]

        if (current_weight == 2 and next_weight == 3) or (current_weight == 3 and next_weight == 2):
            appearence_start_and_end_time.append(time[0])

        current_weight = next_weight

    if len(appearence_start_and_end_time) % 2 != 0 and appearence_start_and_end_time[-1] <= intervals['lesson'][1]:
        appearence_start_and_end_time.append(intervals['lesson'][1])

    return appearence_start_and_end_time


def get_appearance(intervals: dict) -> int:
    """
        return sum of joint intervals(list[int])
    """
    current_intervals = get_total_interval_time(intervals)
    sum_of_current_interval = []
    idx = 1

    while idx < len(current_intervals):
        sum_of_current_interval.append(current_intervals[idx] - current_intervals[idx-1])
        idx += 2

    return sum(sum_of_current_interval)


def appearance(intervals: dict) -> int:
    return get_appearance(intervals)


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]


# if __name__ == '__main__':
#    for i, test in enumerate(tests):
#        test_answer = appearance(test['intervals'])
#        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'