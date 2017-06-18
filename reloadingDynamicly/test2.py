import test1
import importlib

test1.printer("sad")

with open('test1.py', 'w') as f:
	f.writelines('def printer(x):')
	f.writelines('\tprint("sadness is real", x)')
	f.close()

importlib.reload(test1)
test1.printer("sad")

#revert old file
with open('test1.py', 'w') as f:
	f.writelines('def printer(x):')
	f.writelines('\n\tprint(x)')
	f.close()
