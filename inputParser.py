
#reads a text file and return a list of words.
#TODO add ability to process different input sources (scrape twitter, user input, etc), done through subclassing?
class InputParser:

    #we will dump the input text into a words list.
    words = []

    #create this object and pass in the file location of the input txt file.
    def __init__(self, txtFileLocation):
        self.__readTxtFile(txtFileLocation)

    #TODO strip punctuation

    #characters we don't want to process.
    exclude = [ "\'", "\'", "[", "]", ")", "("]

    #parse the text file line by line and add each word to our words list.
    def __readTxtFile(self, txtFileLocation):
        lines = open(txtFileLocation).read().splitlines()
        for line in lines:
            #ignore empty lines.
            if line:
                #hack for how our current input is structured (song lyrics line by line)
                #add a period to the end of every line so when we build sentences they
                #generally match the song lyric structure.
                if line[-1] not in ["!", ".", "?"]:
                    line += "."
                #strp excluded characters from each word and append its lowecase version to our word list.
                for word in line.split():
                     self.words.append(''.join(character for character in word.lower() if character not in self.exclude));