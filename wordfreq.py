def tokenize(text):
    text = "".join(text).lower()
    tokens = []
    current_token = ""
    current_type = None

    for i in text:
        if i.isalpha():
            typ = "alpha"
            if current_type == typ or current_type is None:
                current_token += i
                current_type = typ
            else:
                tokens.append(current_token)
                current_token = i
                current_type = typ
        elif i.isdigit():
            typ = "digit"
            if current_type == typ or current_type is None:
                current_token += i
                current_type = typ
            else:
                tokens.append(current_token)
                current_token = i
                current_type = typ
        else:
            if current_token:
                tokens.append(current_token)
                current_token = ""
                current_type = None
            if not i.isspace():
                tokens.append(i)

    if current_token:
        tokens.append(current_token)


    return tokens

#print(tokenize("baddis is best is the number1!"))