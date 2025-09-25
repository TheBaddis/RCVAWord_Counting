import wordfreq
import sys
import urllib.request

def main():
    stop_file = open(sys.argv[1])
    inp_arg = sys.argv[2]
    limit_num = int(sys.argv[3])

    if inp_arg.startswith(("http", "https")):
        response = urllib.request.urlopen(sys.argv[2])
        lines = response.read().decode("utf8").splitlines()
        tokens = wordfreq.tokenize(lines)
    else:
        inp_file = open(sys.argv[2])
        tokens = wordfreq.tokenize(inp_file)
        inp_file.close()

    stopWords = []
    for stopWord in stop_file:
        stopWords.append(stopWord.strip("\n").lower())
                         
    countedWords = wordfreq.countWords(tokens, stopWords)

    wordfreq.printTopMost(countedWords, limit_num)
    
    stop_file.close()
    
main()
