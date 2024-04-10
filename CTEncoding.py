def tobinary(string):
	bin_string = ''
	for char in string:
		bin_string += bin(ord(char))[2:].zfill(8)
	return bin_string


