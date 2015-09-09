def func():
	global x
	
	print 'x is', x
	x = 2
	print 'x changed to', x

x = 50
func()
print 'value of global var x is', x
