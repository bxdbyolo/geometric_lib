import circle
import square
import triangle


figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']
sizes = {
    "area-circle": 1,
    "area-square": 1,
    "area-triangle": 3,

    "perimeter-circle": 1,
    "perimeter-square": 1,
    "perimeter-triangle": 3,
}


def validate_sides(fig, size):
    if fig == 'circle' or fig == 'square':
        if any(s <= 0 for s in size):
            raise ValueError("Sizes must be positive")
    elif fig == 'triangle':
        a, b, c = size
        if any(s <= 0 for s in size):
            raise ValueError("Sizes must be positive")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Given sides do not form valid triangle")


def calc(fig, func, size):
    assert fig in figs
    assert func in funcs

    validate_sides(fig, size)

    return eval(f'{fig}.{func}(*{size})')


if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Input figure sizes separated by space, "
                                   "1 for circle and square\n").split()))

    result = calc(fig, func, size)
    print(result)
