def half(x):
	x = x // 2
	return x

def hcube(x):
	x = x ** 3
	x = half(x)
	return x

x = 5
y = hcube(x)