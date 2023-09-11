import pytest

from task3.solution import get_persons_time, get_total_interval_time, get_appearance


@pytest.mark.parametrize(
    'data, result',
    [
        (
            {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
             [(1594692000, 1), (1594692017, 1), (1594692033, 1), (1594692066, -1), (1594692068, 1), (1594695600, -1)]
        ),
    ]
)
def test_get_persons_time(data, result):
    """Test retrieving a sorted list[tuple] where [0] is a time and [1] is its weight"""
    res = get_persons_time(data)
    assert res == result


@pytest.mark.parametrize(
    'data, result',
    [
        (
            {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
            [1594692033, 1594692066, 1594692068, 1594695600]
        )
    ]
)
def test_get_total_interval_time(data, result):
    """
        Test retrieving a list of a start and end time where tutor and pupil are together

        (use this list[tuple] in a time sampling)
        data -> [(1594692000, 1), (1594692017, 1), (1594692033, 1), (1594692066, -1), (1594692068, 1), (1594695600, -1)] 
    """
    res = get_total_interval_time(data)
    assert res == result



@pytest.mark.parametrize(
    'data, result',
    [
        (
            {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
            3565
        )
    ]
)
def test_get_appearance(data, result):
    """
        Test retrieving a sum of time intervals
    """
    res = get_appearance(data)
    assert res == result
