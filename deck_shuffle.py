from random import shuffle


class PlayingCards:
    """
    Class to handle card related items
    Functions for shuffling and dealing
    """
    def __init__(self):
        self.deck = [card + suit for card in "A234" for suit in "SC"]
        self.discard_pile = []
        self.hand = []

    def myshuffle(self):
        """
        Function to shuffle discard pile and place it at the bottom of the remaining deck.
        :return:
        """
        shuffle(self.discard_pile)
        self.deck = self.deck + self.discard_pile
        self.discard_pile = []

    def draw_cards(self):
        """
        Function to deal a defined number of cards to the hand
        :param num_card:
        :return:
        """
        card = self.deck.pop()
        return card

    def discard(self, card):
        print(card)
        self.discard_pile.append(card)


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.play_area = []

    def draw(self):
        """
        Draw a card from the current deck and add it to the players hand
        :param deck:
        :return:
        """
        self.hand.append(current_deck.draw_cards())

    def discard(self, card):
        """
        Display the players current hand and choose a card to discard. Then add the chosen card to the discard pile.
        :param card:
        :return:
        """
        self.hand.remove(card)
        current_deck.discard(card)


current_deck = PlayingCards()
player_1 = Player("John")
shuffle(current_deck.deck)
print(current_deck.deck)

while True:
    player_action = input("Do you wish to draw or discard?: ")

    if player_action == "draw":
        player_1.draw()
        print("Player Hand: {}".format(player_1.hand))
    elif player_action == "discard":
        card_choice = input("Which card to you want to discard?: {}".format(player_1.hand))
        if card_choice in player_1.hand:
            player_1.discard(card_choice)
        else:
            print("You don't appear to have that card to discard")
    else:
        print("That wasn't an option")

    # num_cards = input("How many cards: ")
    # num_cards = int(num_cards)
    # current_deck.discard = current_deck.discard + current_deck.hand
    # current_deck.hand = []

    #
    # if num_cards > len(current_deck.deck):
    #     current_deck.myshuffle()
    #     current_deck.draw_cards(num_cards)
    # else:
    #
    #     current_deck.draw_cards(num_cards)

    print(20*"*")
    print("Main Hand: ", player_1.hand)
    print("Main Deck: ", current_deck.deck)
    print("Main Discard: ", current_deck.discard_pile)
    print(20*"*")
