#!/usr/bin/env python3

from collections import deque

def max_sub(arr: list[int], k: int, le: int):
	ind = deque([])
	i = 0
	while (i < k):
		while ind and arr[i] > arr[ind[-1]]:
			ind.pop()
		ind.append(i)
		i += 1
	print('[' + str(arr[ind[0]]), end='')
	while i < le:
		while ind and ind[0] < i - k + 1:
			ind.popleft()
		while ind and arr[i] > arr[ind[0]]:
			ind.popleft()
		ind.append(i)
		print(', ' + str(arr[ind[0]]), end='')
		i += 1
	print("]")

if __name__ == "__main__":
	inp = [10, 5, 2, 7, 8, 7]
	max_sub(inp, 3, len(inp))
