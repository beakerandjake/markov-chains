import random
import sys

class MarkovTextGenerator:

    #the word table which is made up of
    #key: a tuple representing two words which appear in succession
    #value: a list of each word which comes after that tuple
    #(NOTE: the value list allows duplicates! that way words which appear more frequently are more likely to be chosen!)
    wordTable = {}

    #All of the punctuation characters that end a sentence.
    sentenceStop = ['.','!','?', '\r','\n']

    def __init__(self, words):
        self.__buildWordTable(words)

    #build the word table dictionary
    def __buildWordTable(self, words):
        for i in range(len(words) - 3):
            #get three words in succession.
            first, second, third = words[i], words[i+1], words[i+2]
            #build a tuple of the first two words (this is the key)
            key = (first, second)

            #add the key if doesn't exist
            if key not in self.wordTable:
                self.wordTable[key] = []

            #append the third word
            self.wordTable[key].append(third)

    #randomly choose a starting key from the wordTable.
    def getStartingWord(self):
        #TODO make more sophisticated. could only select starting words which ACTUALLY start a sentence in the input.
        #TODO dont choose key with empty value.
        #disgusting line.. but basically we choose randomly from all of keys
        #which do not have punctuation in either word.
        return random.choice([key for key in self.wordTable.keys() if key[0][-1] not in self.sentenceStop and key[1][-1] not in self.sentenceStop])

    #use the markov algorithm to generate text.
    def generateSentence(self):
        output = []
        key = self.getStartingWord()

        one, two = key

        #put the first two words in the ouptut.
        output.append(one)
        output.append(two)

        #keep appending words until we hit a sentence stop character, that marks the end of our sentence.
        while True:
            #Stop if our second word ends the sentence.
            if two[-1] in self.sentenceStop:
                break

            try:
                #Choose a random words from our values.
                three = random.choice(self.wordTable[key])
            except KeyError:
                #We coulddddddd get an empty value from the dictionary, that means we choose the very last two words.
                #if thats the case just end the sentnece.
                break

            output.append(three)

            #be sure to check if the chosen word ended the sentence.
            if three[-1] in self.sentenceStop:
                break

            #move one word over
            key = (two, three)
            one, two = key

        #return the sentence and be sure to capitalize it!
        return ' '.join(output).capitalize()



