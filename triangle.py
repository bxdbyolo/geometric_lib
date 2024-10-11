def area(a, h):
    """
    Возвращает площадь треугольника
    (равна половине произведения длины высоты треугольника и длины стороны, к которой проведена высота)

        Параметры:
            a : длина стороны
            h : длина высоты, проведенной к стороне a

        Возвращаемое значение:
            a * h / 2 : площадь треугольника с заданными параметрами
    """
    return a * h / 2


def perimeter(a, b, c):
    """
    Возвращает периметр треугольника
    (равен сумме длин сторон)

        Параметры:
            a : длина первой стороны
            b : длина второй стороны
            c : длина третьей стороны

        Возвращаемое значение:
            a + b + c : периметр треугольника с заданными параметрами
    """
    return a + b + c
