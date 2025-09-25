def tokenize(documentWithTextLines):
    words = []


    for line in documentWithTextLines:
        index = 0

        # print(f"nu kommer raden:{line}")

        while (index < len(line)):
            print(line[index])
            index += 1
    
    return words


# tokenize(["första rad", "andra rad"])