def tokenize(text):
    words = []
    

    for i in text:
        start = 0
        end = 0
        i = i.lower()
  
        while start < len(i):
  
            if i[start].isspace():
                start += 1
                continue
            if i[start].isalpha():
                end = start
                while end < len(i) and i[end].isalpha():
                    end += 1
                words.append(i[start:end])
                start = end
            elif i[start].isdigit():
                end = start
                while end < len(i) and i[end].isdigit():
                    end += 1
                words.append(i[start:end])
                start = end
            else:
                words.append(i[start])
                start += 1
  
    return words

def countWords(words, stopWords):
    frequencies = {}
    
    #goes through the list "words" and continues 
    #if the word is excluded from the list of banned words ("stopWords")
    for word in words:
        if  not word in stopWords:
            #checks if the word isn't already in the dictionary.
            #if it isn't then it adds the word with a frequency of: 1.
            #else it adds 1 to the words frequency value.
            if word not in frequencies:
                frequencies.setdefault(word, 1)
            else:
                frequencies[word] += 1

    return frequencies

def printTopMost(frequencies, n):
    wordList = []
    sortedDict = {}

    #puts the words and their corresponding frequency in seperate tuples 
    #and then the tuples are placed in a list to be sorted
    for word,freq in frequencies.items():
        tupWord = (word.ljust(5), freq)
        wordList.append(tupWord)

    #sorts the list of tuples by size, most frequent first
    sortedList = sorted(wordList, key=lambda x: x[1], reverse=True)

    #removes the bottom most entries in the list as limited by n
    if n <= 0:
        sortedList = []
    else:
        sortedList = sortedList[:n]
        

    #runs through the sorted list and extracts the values form the tuples
    #and places them into a new dictionary, that is now sorted!
    for i in sortedList:
        sortedDict.setdefault(i[0], i[1])
    
    #goes through each item in the sorted dictionary and print the key 
    #and corresponding value in a table
    for word,freq in sortedDict.items():
        print(word.ljust(20), str(freq).rjust(5))

#printTopMost({'text': 9, 'word': 30, 'fiction': 6, 'count': 11, 'counting': 7, 'novel': 6}, 4)