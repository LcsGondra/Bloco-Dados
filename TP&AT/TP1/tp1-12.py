import random
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

random.shuffle(cards)

cards = cards[:5]
def sort_or_not(cards):
    cards_c = cards.copy()
    cards_c.sort()
    cards_d = cards.copy()
    cards_d.sort(reverse=True)
    if cards == cards_c:
        print('C') #crescente
    elif cards == cards_d:
        print('D') #decrescente
    else:
        print('N') #nao ordenada

print(cards)
sort_or_not(cards)
