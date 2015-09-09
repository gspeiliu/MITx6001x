def func(x):
	print 'x is', x
	x = 2
	print 'Changed local var x to', x

x = 50
func(x)
print 'global var still is', x
