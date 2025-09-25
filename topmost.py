import wordfreq
import sys

def main():
    stop_file = open(sys.argv[1])
    inp_file = open(sys.argv[2])
    limit_num = int(sys.argv[3])
    
    stopWords = []
    for stopWord in stop_file:
        stopWords.append(stopWord.strip("\n").lower())
                         
    tokens = wordfreq.tokenize(inp_file)

    countedWords = wordfreq.countWords(tokens, stopWords)

    wordfreq.printTopMost(countedWords, limit_num)
    
    stop_file.close()
    inp_file.close()

main()
