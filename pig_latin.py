# Pig latin translator

def pig_latin(word):
    if word[0].lower() not in 'aeiou':
        word = '{}{}'.format(word[1:], word[0])
    word += 'ay'
    return word


print(pig_latin('Thomas'))


def pig_latin_simple(word):
    first_letter = word[0]
    if first_letter.lower() in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word


print(pig_latin_simple('Thomas'))

def myfunc(word):
    skyline = ''
    for index, letter in enumerate(word):
        if index % 2 == 0:
            skyline += letter
        else:
            skyline += letter.upper()
    return skyline

print(myfunc('hehehehehe'))