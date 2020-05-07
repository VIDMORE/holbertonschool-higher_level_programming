#!/usr/bin/python3
def square_matrix_map(matrix=[]):
	return list(map(lambda listt: list(map(lambda value: value ** 2, listt)), matrix))
