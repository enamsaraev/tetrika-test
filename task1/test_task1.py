import pytest

from task1.solution import strict, sum_two


@pytest.mark.parametrize(
    'val1, val2, result',
    [
        (1, 2, 3),
        (1, 2.4, TypeError),
    ]
)
def test_int(val1, val2, result):
    """
        Test checking for int
    """
    res = sum_two(val1, val2)
    assert res == result


@pytest.mark.parametrize(
    'val1, val2, result',
    [
        (1, 2, TypeError),
        (1, 1, 1),
    ]
)
def test_bool(val1, val2, result):
    """
        Test checking for bool
    """
    @strict
    def sum_bool(a: bool, b: bool) -> bool:
        return a + b
    
    res = sum_bool(val1, val2)
    assert result


@pytest.mark.parametrize(
    'val1, val2, result',
    [
        ('a', 'b', 'ab'),
        (1, 1, TypeError),
    ]
)
def test_str(val1, val2, result):
    """
        Test checking for str
    """
    @strict
    def sum_bool(a: str, b: str) -> bool:
        return a + b
    
    res = sum_bool(val1, val2)
    assert result


@pytest.mark.parametrize(
    'val1, val2, result',
    [
        (1.1, 2, 3.1),
        (1, 1, TypeError),
    ]
)
def test_float(val1, val2, result):
    """
        Test checking for float
    """
    @strict
    def sum_bool(a: float, b: int) -> bool:
        return a + b
    
    res = sum_bool(val1, val2)
    assert result