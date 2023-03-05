#!/usr/bin/env python3

def minRooms(arr: list[list[int]]) -> int:
	start = []
	end = []
	for lst in arr:
		start.append(lst[0])
		end.append(lst[1])
	start.sort()
	end.sort()
	rooms = 0
	endcount = 0
	for i in range(0, len(start)):
		if (start[i] < end[endcount]):
			rooms += 1
		else:
			endcount += 1
	return rooms

if __name__ == "__main__":
	print("[[30, 75], [0, 50], [60, 150]]")
	print("min rooms " + str(minRooms([[30, 75], [0, 50], [60, 150]])))
	print()
	print("[[1, 10], [2, 7], [3, 19], [8, 12], [10, 20], [11, 30]]")
	print("min rooms " + str(minRooms([[1, 10], [2, 7], [3, 19], [8, 12], [10, 20], [11, 30]])))
