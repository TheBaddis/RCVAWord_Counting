import wordfreq
import sys
import urllib.request

def main():
    #reads the arguments provided in the terminal
    stop_file = open(sys.argv[1])
    inp_arg = sys.argv[2]
    limit_num = int(sys.argv[3])

    #Checks if argument 2 (the input text) is a web link or a file.
    #Then opens it with the appropriate method and puts it in a string
    #That string is then used in the tokenize function written in wordfreq
    if inp_arg.startswith(("http", "https")):
        response = urllib.request.urlopen(sys.argv[2])
        lines = response.read().decode("utf8").splitlines()
        tokens = wordfreq.tokenize(lines)
    else:
        inp_file = open(sys.argv[2])
        tokens = wordfreq.tokenize(inp_file)
        inp_file.close()

    #puts the noncounted words in a list
    stopWords = []
    for stopWord in stop_file:
        stopWords.append(stopWord.strip("\n").lower())
                         
    #counts the frequency of the words
    countedWords = wordfreq.countWords(tokens, stopWords)

    #sorts the words by frequency and prints them in a table
    wordfreq.printTopMost(countedWords, limit_num)
    
    stop_file.close()
    
main()
