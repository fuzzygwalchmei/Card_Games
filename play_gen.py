from random import shuffle

start_deck = list(card + suit for card in list("2345") for suit in list("CS"))
discard = []


def get_card(deck):
    global discard
    while True:
        try:
            yield card
            deck.pop()
            discard.append(card)
            print("Deck: ",len(start_deck))

        except StopIteration:
            deck = discard
            list(shuffle(deck))
            print("shuffled")


deck = start_deck
shuffle(deck)
print(deck)
PlayingDeck = get_card(deck)

for each in range(20):
    print(each, ": ", next(PlayingDeck))
    print(discard)
