import re
def infinite_delim(alphabet, _string):
	end = []
	end2 = []
	delim = []
	for k in _string:
		if not k in alphabet:
			if not k in delim:
				delim.append(k)

	_string = _string.split(delim[0])

	for x in _string:
		end.append(x)

	for z in range(1, len(delim)):
		for x in end:
			temp = x
			x = x.split(delim[z])
			if len(x) > 1:
				end.remove(temp)
				for k in x:
					end.append(k)

	end=set(end)

	for x in end:
		if not x == '':
			x = x.strip()
			end2.append(x)

	return end2

_string = "плиз, класк, swag: sgae\sad, tis's1's2/bej]sad"
alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЗЧШЩЪЬЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890абвгдежзийклмнопрстуфхцчшщъьюяabcdefghijklmnopqrstuvwxyz'' "

print(_string)
end = infinite_delim(alphabet, _string)
print(end)