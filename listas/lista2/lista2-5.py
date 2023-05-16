import random
def embaralhar(pal):
    pal.lower()
    pal = list(pal)
    random.shuffle(pal)
    print(''.join(pal))

embaralhar(input('palavra para embaralhar: '))
