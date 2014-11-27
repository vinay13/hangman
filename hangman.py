import random
HANGMANPICS=['''

    +---+
    |   |
        |
        |
        |
        |
  ==========''','''

    +---+
    |   |
    O   |
        |
        |
        |
  ============''','''


    +---+
    |   |
    O   |
    |   |
        |
        |
  ============''','''



    +---+
    |   |
    O   |
   /|   |
        |
        |
  ============''','''


    +---+
    |   |
    O   |
   /|\  |
        |
        |
  ============''','''




    +---+
    |   |
    O   |
   /|\  |
   /     |
        |
  ============''','''


    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  ============''']
    

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar
coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion
lizard llama mole monkey moose mouse mule newt otter owl panda parrot
pigeon python rabbit ram rat raven
rhino salmon seal shark sheep skunk
sloth snake spider stork swan tiger toad trout turkey turtle weasel whale
wolf wombat zebra'.split()


def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList)-1)
    return wordList[wordIndex]
    def displayBoard(HANGMANPICS, missedLetters, correctLetters,
secretWord):
        print(HANGMANPICS[len(missedLetters)])
        print()

        print 'missed letters:',end=' '
        for letter in missedLetters:
            print letter,end=' '
        print
        blanks='_'+len(secretWord)

        for i in range(len(secretWord)):   #replace blanks with correctly guessed letters
            if secretWord[i] in correctLetters:
                blanks=blanks[:i]+secretWord[i]+blanks[i+1:]

        for letter in blanks: #show secret word with spaces in between each other
            print letter,end=' '
        print

    def getGuess(alreadyGuessed):
        while True:
            print 'guess a letter'
            guess =input()
            guess=guess.lower()
            if len(guess)!=1:
                print 'please enter a single letter'
            elif guess in alreadyGuessed:
                print 'you have already guessed the letter.'
            elif guess not in 'abcdefghimnopqrst':
                print 'please enter a LEtter'
            else:
                return guess

    def playAgain():
        print 'Do you want to play again?(yes or no)'
        return input().lower().startswith('y')
            

