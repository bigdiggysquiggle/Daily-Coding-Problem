#!/usr/bin/env python3

def enc_count(st):
	if len(st) > 1:
		count = count_help(st[1:]) + count_help(st[2:])
	elif (st > 1):
		return 1
	return count

def count_help(st):
	if len(st) < 2:
		return 1
	count = 0
	if st[0] > "0" and st[0] < "3":
		count += count_help(st[2:])
	return count + count_help(st[1:])

if __name__ == '__main__':
	test = "111"
	print(enc_count(test))
	print(enc_count("9135022905932091"))
