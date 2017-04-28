import sys

def my_excepthook(_type, value, traceback):
	print("*" * 50)
	print("The type of the exception is: ", _type)
	print("The value of the exception is: ", value)
	print("The traceback is: ", traceback)
	print("*" * 50)

def abc(a, b):
	pass

sys.excepthook = my_excepthook
a = 15
try:
	abc(a)
except Exception as e:
	print(e)

print(50/0)