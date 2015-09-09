def howMany(aDict):
    res = 0
    for e in aDict:
        res = res + len(aDict[e])
        
    return res;
  

def howMany2(aDict):
    res = 0
    for value in aDict.values():
        print value
        res += len(value)
        
    return res
    

def biggest(aDict):
    res = ''
    temp = -1
    for key in aDict:
        if len(aDict[key]) > temp:
            temp = len(aDict[key])
            res = key
    if res != '':
        return res
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
print animals.values()
print howMany(animals)
print howMany2(animals)
print biggest({})