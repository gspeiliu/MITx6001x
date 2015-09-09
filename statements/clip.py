def clip(lo, x, hi):
    while min(lo, x, hi) < lo:
        return lo
    while max(lo, x, hi) > hi:
        return hi
    return x
    
print clip(3, 4, 5)
print clip(4, 3, 5)
print clip(3, 5, 4)

a = 10
def f(x):
    return x + a
a = 3

print f(1)

x = 12
def g(x):
    x = x + 1
    def h(y):
        return x + y
    return h(6)
    
print g(x)

def isVowel(char):
    if char == 'a' or char == 'A' or\
    char == 'e' or char == 'E' or \
    char == 'i' or char == 'I'or \
    char == 'o' or char == 'O'or \
    char == 'u' or char == 'U':
        return True
    return False
    
def isVowel2(char):
    if char in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        return True
    return False
    
print isVowel2('a')

def strcnt(s):
    i = 0
    res = 0
    while True:
        temp = s.find('bob', i)
        if temp == -1:
            break;
 #       print i
        res += 1
        i = temp + 2
        
    return res

print strcnt('robobrbgtuobobbizjoxuboboboobboob')

def strLong(s):
    res = s[0]
    i = 1
    resLen = 1
    temp = 1
    resStr = s[0]
    #print len(s)
    while i < len(s):
       # print i
        if s[i] >= s[i - 1]:
    #        print s[i] + s[i - 1]
            temp += 1
            res = res + s[i]
        #    print res
            if temp > resLen:
                resLen = temp
                resStr = res
        else:
            res = s[i]
            temp = 1
        i += 1
    return resStr
     
#print 'Longest substring in alphabetical order is: ' + strLong(s) 
print strLong('abcdefghijklmnopqrstuvwxyz')


def compute(balance, annualInterestRate, monthlyPaymentRate):
    i = 1
    total = 0
    remain = balance
    while i < 13:
        monthPay = balance * monthlyPaymentRate
        total = total + monthPay
        balance = (balance - monthPay) * (1 + (annualInterestRate / 12.0))
        print 'Month: ' + str(round(i, 2))
        print 'Minimum monthly payment: ' + str(round(monthPay, 2))
        print 'Remaining balance: ' + str(round(balance, 2))
        i += 1
        remain = balance
    print 'Total paid: ' + str(round(total, 2))
    print 'Remaining balance: ' + str(round(remain, 2))
        
compute(4213, 0.2, 0.04)

def compute2(balance, annualInterestRate):
    i = 10
   # print pow(2, 4)
    interest = 1 + annualInterestRate / 12.0
    #print pow(interest, 12)
    while (balance - i) * pow(interest, 12) -\
    i * pow(interest, 11) - \
    i * pow(interest, 10) - \
    i * pow(interest, 9) - \
    i * pow(interest, 8) - \
    i * pow(interest, 7) - \
    i * pow(interest, 6) - \
    i * pow(interest, 5) - \
    i * pow(interest, 4) - \
    i * pow(interest, 3) - \
    i * pow(interest, 2) - \
    i * pow(interest, 1) >= 0:
        i = i + 10
    return i
        
def compute3(balance, annualInterestRate):
    lo = balance / 12.0
    interest = 1 + annualInterestRate / 12.0
    high = balance * pow((1 + (annualInterestRate) / 12.0), 12) / 12.0
   # print high
    while True:
        i = (high + lo) / 2.0
       # print i
        temp = (balance - i) * pow(interest, 12) -\
    i * pow(interest, 11) - \
    i * pow(interest, 10) - \
    i * pow(interest, 9) - \
    i * pow(interest, 8) - \
    i * pow(interest, 7) - \
    i * pow(interest, 6) - \
    i * pow(interest, 5) - \
    i * pow(interest, 4) - \
    i * pow(interest, 3) - \
    i * pow(interest, 2) - \
    i * pow(interest, 1)
       # print temp
        if temp < 0:
            if abs(temp) < 0.01:
                return i
            else:
                high = i
        else:
            lo = i     

print 'Lowest Payment: ' + str(round(compute3(320000, 0.2), 2))

def iterPower(base, exp):
    res = 1
    while exp > 0:  
        res = res * base
        exp -= 1
    return res


def recurPower(base, exp):
    if exp == 0:
        return 1
    return base * recurPower(base, exp - 1)

def recurPowerNew(base, exp):
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        return recurPowerNew(base * base, exp / 2)
    else:
        return base * recurPowerNew(base, exp - 1)

print recurPowerNew(-5.08, 9)
              
def gcdIter(a, b):
    smaller = min(a, b)
    while True:
        if a % smaller == 0 and b % smaller == 0:
            return smaller
        else:
            smaller -= 1 
            
def gcdRecur(a, b):
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

def lenIter(aStr):
    if aStr == '':
        return 0
    pos = aStr.rindex(aStr[-1])
    return pos + 1
    
def lenRecur(aStr):
    if aStr == '':
        return 0
    return 1 + lenRecur(aStr[1:])

def isIn(char, aStr):
    if aStr == '':
        return False
    lo = 0
    hi = len(aStr)
    half = (lo + hi) / 2
    #print 'lo = ' + str(lo) + ' hi = ' + str(hi)
    if char == aStr[half]:
        return True
    else:     
        if char < aStr[half]:
            return isIn(char, aStr[:half])
        elif char > aStr[half]:
            return isIn(char, aStr[half + 1:])
            
def semordnilap(str1, str2):
    if len(str1) != len(str2):
        return False
    if str1 == '':
        return True
    return str1[0] == str2[len(str2) - 1] and semordnilap(str1[1:], str2[:len(str2) - 1])
    

def oddTuples(aTuples):
    i = 0
    res = ()
    for d in aTuples:
        if i % 2 == 0:
            res = res + (d,)
        i += 1
            
    return res

aTp = ('gos', 'abs', 'dfg')

print oddTuples((17,))

    
