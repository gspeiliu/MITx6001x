low = 0
high = 100
half = 50
print 'Please think of a number between 0 and 100!'
print 'Is your secret number 50?'
print "Enter 'h' to indicate the guess is too high.\
 Enter 'l' to indicate the guess is too low. Enter 'c'\
 to indicate I guessed correctly." ,
charin = str(raw_input())
while True:
    if charin == 'h':
        high = half
        half = (low + high) / 2
        print 'Is your secret number ' + str(half)
        print "Enter 'h' to indicate the guess is too high.\
 Enter 'l' to indicate the guess is too low. Enter 'c'\
 to indicate I guessed correctly." ,
    elif charin == 'l':
        low = half
        half = (low + high) / 2
        print 'Is your secret number ' + str(half)
        print "Enter 'h' to indicate the guess is too high.\
 Enter 'l' to indicate the guess is too low. Enter 'c'\
 to indicate I guessed correctly." ,
    elif charin == 'c':
        print 'Game over.',
        print 'Your secret number was: ' + str(half)
        break;
    else:
        print 'Sorry, I did not understand your input.'
        print 'Is your secret number ' + str(half) + '?'
        print "Enter 'h' to indicate the guess is too high.\
 Enter 'l' to indicate the guess is too low. Enter 'c'\
 to indicate I guessed correctly." ,
    charin = str(raw_input())