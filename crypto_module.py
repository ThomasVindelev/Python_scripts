lowercase = ["a", "b", "c", "d", "e", "f",
             "g", "h", "i", "j", "k", "l",
             "m", "n", "o", "p", "q", "r",
             "s", "t", "u", "v", "w", "x",
             "y", "z", "æ", "ø", "å"]

uppercase = [x.upper() for x in lowercase]


def encrypt(to_encrypt, number):

    new_word = ""
    new_char = ""

    for l in to_encrypt:
        if l.isupper():
            index = uppercase.index(l)
            if len(uppercase) - 1 < index + number:
                new_char = uppercase[(index + number) - len(uppercase)]
            else:
                new_char = uppercase[index + number]
            new_word += new_char
        elif l.islower():
            index = lowercase.index(l)
            if len(lowercase) - 1 < index + number:
                new_char = lowercase[(index + number) - len(lowercase)]
            else:
                new_char = lowercase[index + number]
            new_word += new_char
        else:
            new_word += l
    return new_word


def decrypt(to_decrypt, number):

    new_word = ""
    new_char = ""

    for l in to_decrypt:
        if l.isupper():
            index = uppercase.index(l)
            if 0 > index - number:
                new_char = uppercase[(index - number) + len(uppercase)]
            else:
                new_char = uppercase[index - number]
            new_word += new_char
        elif l.islower():
            index = lowercase.index(l)
            if 0 > index - number:
                new_char = lowercase[(index - number) + len(lowercase)]
            else:
                new_char = lowercase[index - number]
            new_word += new_char
        else:
            new_word += l
    return new_word

