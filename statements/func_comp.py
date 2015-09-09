def a(x, y, z):
     if x:
         print 'exe?'
         return y
     else:
         print 'How'
         return z

def b(q, r):
    return a(q>r, q, r)
    
#a(3 > 2, a, b)


#b(a, b)