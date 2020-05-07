#!/usr/bin/python3
def square_matrix_map(matrix=[]):
	return list(map(lambda list: list(map(lambda value: value ** 2, list)), matrix))
