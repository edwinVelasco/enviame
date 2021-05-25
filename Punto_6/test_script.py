import pytest
from script import get_days

@pytest.mark.parametrize("km, exp", [
    (50, 0),
    (150, 1),
    (250, 1),
    (390, 2),
    (490, 3),
    (1850, 2584),
])
def test_get_days(km, exp):
    days = get_days(km)
    assert type(days) == int
    assert days == exp


