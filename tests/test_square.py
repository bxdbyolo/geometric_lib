import pytest
import sys
sys.path.append('..')

from calculate import calc

#square tests
@pytest.mark.parametrize("size, expected, is_correct", [
    ([3], 9, True),
    ([3], 6, False),
    ([-3], 9, "invalid"),
    ([5], 25, True)
])
def test_square_area(size, expected, is_correct):
    try:
        if is_correct:
            assert calc("square", "area", size) == expected
        else:
            assert calc("square", "area", size) != expected
    except ValueError as e:
        print(f" Error: {e}")

@pytest.mark.parametrize("size, expected, is_correct", [
    ([3], 12, True),
    ([3], 6, False),
    ([-3], -12, "invalid"),
    ([5], 20, True)
])
def test_square_perimeter(size, expected, is_correct):
    try:
        if is_correct:
            assert calc("square", "perimeter", size) == expected
        else:
            assert calc("square", "perimeter", size) != expected
    except ValueError as e:
        print(f" Error: {e}")