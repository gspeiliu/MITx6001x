def f(x):
    import math
    return 10 * math.e ** (math.log(0.5)/5.27*x)


def radiationExposure(start, stop, step):
    res = 0
    i = 0;
    while i < (stop - start) / step:
        res += f(start + i * step)
        i += 1
    return res * step
    
    
def radiationExposure2(start, stop, step):
    res = 0
    i = 0;
    while start < stop:
        res += f(start)
        start += step
    return res * step
    
print radiationExposure(12, 16, 1)
print radiationExposure2(12, 16, 1)