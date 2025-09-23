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
#print(tokenize(["This is a simple sentence"]))