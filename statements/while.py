#!/usr/bin/python
#Filename: if.py
 
number = 23
running = True

while running:
    guess = int(raw_input('Enter an integer:'))

    if guess == number:
               print 'Congratulations, you guessed it.'
               print '( but you do not win any prizes! )'
	       running = False
    elif guess < number:
           print 'No, it is a litter higher than that'
    else:
        print 'No, it is a litter lower than that'
else:
 print 'The while loop is over.'

print 'Done'
