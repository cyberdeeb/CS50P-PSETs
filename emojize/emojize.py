import emoji

def emojize():
    word = input('Input: ')
    print(f'Output: {emoji.emojize(word)}')

emojize()