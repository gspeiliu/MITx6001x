# -*- coding: utf-8 -*-
def FancyDivide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [SimpleDivide(item, denom)
               for item in list_of_numbers]


def SimpleDivide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0
        
print FancyDivide([0, 2, 4], 0)

def Normalize(numbers):
    max_number = max(numbers)
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
    return numbers   
    
try:
      Normalize([0, 0, 0])
except ZeroDivisionError, e:
      print 'Invalid maximum element'