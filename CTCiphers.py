def caesar_cipher(string):
	alph = 'abcdefghijklmnopqrstuvwxyz'
	cap_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	all_shifts = []

	for shift in range(1, 27):
		encrypted_string = ""
		for char in string:
			if char in alph:
				idx = (alph.index(char) + shift) % 26
				encrypted_string += alph[idx]
			elif char in cap_alph:
				idx = (cap_alph.index(char) + shift) % 26
				encrypted_string += cap_alph[idx]
			else:
				encrypted_string += char
		all_shifts.append(encrypted_string)

	x = ''
	for shift,cipher in enumerate(all_shifts, start=1):
		x = x + f"Shift {shift}: {cipher} $ "
	return x
