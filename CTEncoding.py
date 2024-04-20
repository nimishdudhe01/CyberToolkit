from math import ceil

def tobinary(string):
	bin_string = ''
	for char in string:
		bin_string += bin(ord(char))[2:].zfill(8)
	return bin_string

def tobase64(string):
	charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
	pad = '='
	base64_string = ''
	bin_string = tobinary(string)
	for i in range(ceil(len(bin_string)/6)):
		string = bin_string[i*6:(i+1)*6].ljust(6,'0')
		base64_string += charset[int(string,2)]
	string = padding(base64_string, 4 - (len(base64_string)%4), pad)
	return string

def padding(string=str, number=int, pad=str):
	for i in range(number):
		string += pad
	return string