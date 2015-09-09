from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#

def isValidWordB(word, hand):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    temp = hand.copy()
    for e in word:
        if temp.get(e, 0) == 0:
            return False
        else:
            temp[e] -= 1
    return True

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0

    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = ''

    # For each word in the wordList
    for word in wordList:
        if isValidWordB(word, hand):
            if getWordScore(word, n) > maxScore:
                maxScore = getWordScore(word, n)
                bestWord = word
    if bestWord != '':
        return bestWord

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)

            # Find out how much making that word is worth

            # If the score for that word is higher than your best score

                # Update your best score, and best word accordingly


    # return the best word you found.


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    total = 0
    while True:
        if calculateHandlen(hand) == 0:
            break
        print 'Current Hand: ',
        displayHand(hand)
        word = compChooseWord(hand, wordList, n)
        if word != None:
            score = getWordScore(word, n)
            total += score
            print '"' + word + '"' + ' earned ' + str(score) +' points. Total: ' + str(total) + ' points'
            hand = updateHand(hand, word)
        else:
            break
    print 'Total: ' + str(total) + ' points.'
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    #print "playGame not yet implemented." # <-- Remove this when you code this function
    n = HAND_SIZE
    hand = {}
    while True:
        strIn = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        
        while not strIn in ['n', 'r', 'e']:
            print 'Invalid command.'
            strIn = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if strIn == 'e':
            break
        if strIn == 'n':
            hand = dealHand(n)
        if not hand:
                print 'You have not played a hand yet. Please play a new hand first!'
                continue
        print
        strRole = raw_input('Enter u to have yourself play, c to have the computer play: ')
        while not strRole in ['u', 'c']:
            print 'Invalid command.'
            strRole = raw_input('Enter u to have yourself play, c to have the computer play: ')
        print
        if strRole == 'c':
            compPlayHand(hand, wordList, n)
        else:
            playHand(hand, wordList, n)
        print
        

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    #print compChooseWord({'x': 2, 'z': 2, 'q': 2, 'n': 2, 't': 2}, wordList, 12)
    #compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
    playGame(wordList)


