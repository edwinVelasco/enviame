import pytest
from script import get_divider, get_next_fibonachi

@pytest.mark.parametrize("number, exp", [
    (12, 6), 
    (21, 4), 
    (50, 6),
])
def test_get_divider(number, exp):
    response = get_divider(number)
    assert type(response) == int
    assert response == exp
    

@pytest.mark.parametrize("list_f, exp", [
    ([1, 1], [1, 2]), 
    ([1, 2], [2, 3]), 
    ([8, 13], [13, 21]),
])
def test_get_next_fibonachi(list_f, exp):
    response = get_next_fibonachi(list_f=list_f)
    assert type(response) == list
    assert response == exp
