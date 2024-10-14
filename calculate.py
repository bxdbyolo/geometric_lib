import circle
import square


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
	"""
	Рассчитывает площадь/периметр для указанной фигуры с заданными параметрами.

		Параметры:
			fig : название фигуры
			func : функция, которую мы хотим применить к фигуре (периметр/площадь)
			size : параметры, необходимые для расчета выбранной функции

		Высчитывает результат через eval, затем выводит его в консоль.
	"""

	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, available are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, available are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)
