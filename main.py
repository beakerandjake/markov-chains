import random
from inputParser import InputParser
from markovTextGenerator import MarkovTextGenerator

#use the InputParser to generate a word list of the input text file.
#parser = InputParser("wutang.txt")
parser = InputParser("beatles.txt")
#feed this word list to the markovGenerator.
markovGenerator = MarkovTextGenerator(parser.words)

#For now we are hard coding generation of songs as a test.
linesInVerse = 5
numberOfVerses = 5

#Generate X verses of Y sentences per verse.
for verse in range(numberOfVerses):
    for sentence in range(linesInVerse):
        print(markovGenerator.generateSentence())

    #add a line break between verses.
    print()
