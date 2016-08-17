def f(**kwargs):
	for d in kwargs:
		for k in kwargs.get(d):
			print(k + ": " + kwargs.get(d).get(k))

magic_dict = {"apple": "1","sadness": "2","third": "sadness","pesho": "etc"}

f(magic = magic_dict)