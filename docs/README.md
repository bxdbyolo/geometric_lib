# Документация к проекту
В данном проекте на языке **python** реализованы функции для вычисления площади и периметра разных геометрических фигур, а именно: окружности, квадрата и треугольника.

# Описание работы функций
## 1. Окружность (circle.py)
### Площадь
#### Аргументы
```
r : радиус окружности
```
#### Реализация
```python
import math
def area(r):
    return math.pi * r * r 
```
### Периметр
#### Аргументы
```
r : радиус окружности
```
#### Реализация
```python
def perimeter(r):
    import math
    return 2 * math.pi * r 
```
## 2. Квадрат (square.py)
### Площадь
#### Аргументы
```
a : длина стороны квадрата
```
#### Реализация
```python
def area(a): 
    return a * a
```
### Периметр
#### Аргументы
```
a : длина стороны квадрата
```
#### Реализация
```python
def perimeter(a): 
    return 4 * a
```
## 3. Треугольник (triangle.py)
### Площадь
#### Аргументы
```
a : длина основания
h : высота, проведённая к основанию
```
#### Реализация
```python
def area(a, h): 
    return a * h / 2 
```
### Периметр
#### Аргументы
```
a (int): длина первой стороны
b (int): длина второй стороны
c (int): длина третьей стороны
```
#### Реализация
```python
def perimeter(a, b, c): 
	return a + b + c
```

# История коммитов
+ **bb0d22331211cb23826bcb91253d6569c7f23610** - Documentation in program files added
+ **1c2cd7c5c3b38e197d92da12480584dc1b00826e** - fixed triangle's area function
+ **b5b0fae727ca72c317c383b39c0af73d6adcd81c** - L-04: Update docs for calculate.py
+ **d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71** - L-04: Add calculate.py
+ **51c40ebfd0e0b65f52fe5e54740cbb038e492db3** - L-04: Doc updated for triangle
+ **d080c7888b81955bad2ed78d58ad910526b5132a** - L-04: Triangle added
+ **d078c8d9ee6155f3cb0e577d28d337b791de28e2** - L-03: Docs added
+ **8ba9aeb3cea847b63a91ac378a2a6db758682460** - L-03: Circle and square added
