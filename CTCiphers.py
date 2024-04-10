alph = 'abcdefghijklmnopqrstuvwxyz'
cap_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesar_cipher(string):
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

	shifts = ''
	for shift,cipher in enumerate(all_shifts, start=1):
		shifts += f"Shift {shift}: {cipher} $ "
	return shifts

def atbash_cipher(string):
	encrypted_string = ''
	for char in string:
		if char in alph:
			idx = 26 - 1 - (alph.index(char))
			encrypted_string += alph[idx]
		elif char in cap_alph:
			idx = 26 - 1 - (cap_alph.index(char))
			encrypted_string += cap_alph[idx]
		else:
			encrypted_string += char

	return encrypted_string
