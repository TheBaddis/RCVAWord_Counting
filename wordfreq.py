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
    
    for word in words:
        if  not word in stopWords:
            if word not in frequencies:
                frequencies.setdefault(word, 1)
            else:
                frequencies[word] += 1

    return frequencies

def printTopMost(frequencies, n):
    wordList = []
    i = 0
    sortedDict = {}
    
    for word,freq in frequencies.items():
        if n > i:
            tupWord = (word.ljust(5), freq)
            wordList.append(tupWord)
        i += 1

    sortedList = sorted(wordList, key=lambda x: x[1], reverse=True)

#behöver ta tuples i sortedList och stoppa in i en dict

    for i in sortedList:
        if word not in frequencies:
            frequencies.setdefault(word, 1)
        else:
            frequencies[word] += 1
        
    return sortedDict.items()
print(printTopMost({"clean":1,"water":2,"drinkable":3}, 3))