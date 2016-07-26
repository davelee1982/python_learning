def translate():
    word = ''
    while len(word) < 2:
        word = input('Enter a word with at least 2 characters: ').lower()
    first = word[0]
    second = word[1].upper()
    prefix = second + word[2:]
    suffix = first + 'ay'
    new_word = prefix + suffix
        
    if len(word) > 1 and word.isalpha():
        print('Pyglatin translation:', new_word, '\n')
        translate()
    else:
        print('Invalid Entry!\n')
        translate()

translate()
