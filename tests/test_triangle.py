import pytest
import sys

sys.path.append('../geometric_lib')

from ..calculate import calc

# triangle tests
@pytest.mark.parametrize("size, expected, is_correct", [
    ([3, 4, 5], 6, True),
    ([1, 2, 3], 0, "invalid"),
    ([3, 4, 5], 5, False),
    ([-3, -4, 5], 6, "invalid")
])
def test_triangle_area(size, expected, is_correct):
    try:
        if is_correct:
            assert calc("triangle", "area", size) == expected
        else:
            assert calc("triangle", "area", size) != expected
    except ValueError as e:
        print(f" Error: {e}")

@pytest.mark.parametrize("size, expected, is_correct", [
    ([3, 4, 5], 12, True),
    ([1, 2, 3], 0, "invalid"),
    ([3, 4, 5], 10, False),
    ([-3, -4, 5], 0, "invalid")
])
def test_triangle_perimeter(size, expected, is_correct):
    try:
        if is_correct:
            assert calc("triangle", "perimeter", size) == expected
        else:
            assert calc("triangle", "perimeter", size) != expected
    except ValueError as e:
        print(f" Error: {e}")