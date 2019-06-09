from random import shuffle


class PlayingCards:

    def __init__(self):
        self.deck = [card + suit for card in "A234" for suit in "SC"]
        self.discard = []
        self.hand = []

    def myshuffle(self):
        shuffle(self.discard)
        self.deck = self.deck + self.discard
        self.discard = []

    def draw_cards(self, num_card):

        for card in range(num_card):
            card = self.deck.pop()
            self.hand.append(card)


current_deck = PlayingCards()

print(current_deck)

while True:
    num_cards = input("How many cards: ")
    num_cards = int(num_cards)
    current_deck.discard = current_deck.discard + current_deck.hand
    current_deck.hand = []

    if num_cards > len(current_deck.deck):
        current_deck.myshuffle()
        current_deck.draw_cards(num_cards)
    else:

        current_deck.draw_cards(num_cards)

    print("Main Hand: ", current_deck.hand)
    print("Main Deck: ", current_deck.deck)
    print("Main Discard: ", current_deck.discard)