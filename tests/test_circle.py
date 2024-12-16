import pytest

from ..calculate import calc

# circle tests
@pytest.mark.parametrize("size, expected, is_correct", [
    ([3], 28.274333882308138, True),
    ([3], 33, False),
    ([-3], -28, "invalid"),
    ([5], 78.53981633974483, True)
])
def test_circle_area(size, expected, is_correct):
    try:
        if is_correct:
            assert calc("circle", "area", size) == expected
        else:
            assert calc("circle", "area", size) != expected
    except ValueError as e:
        print(f" Error: {e}")

@pytest.mark.parametrize("size, expected, is_correct", [
    ([3], 18.84955592153876, True),
    ([3], 19, False),
    ([-3], -18.84955592153876, "invalid"),
    ([5], 31.41592653589793, True)
])
def test_circle_perimeter(size, expected, is_correct):
    try:
        if is_correct:
            assert calc("circle", "perimeter", size) == expected
        else:
            assert calc("circle", "perimeter", size) != expected
    except ValueError as e:
        print(f" Error: {e}")