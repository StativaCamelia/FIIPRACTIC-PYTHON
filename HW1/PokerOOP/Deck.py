import random

from Card import Card, RANKS, SUITS


class Deck:
	def __init__(self):
		self.deck = []

	def start_deck(self):
		self.deck = [Card(rank, suit) for rank in RANKS for suit in SUITS]

	def shuffle_deck(self):
		return random.shuffle(self.deck)

	def get_card(self):
		return self.deck.pop(0)

	def get_set_of_cards(self, n):
		if n <= len(self.deck):
			return [self.get_card() for _ in range(n)]


deck = Deck()
deck.start_deck()
deck.get_set_of_cards(3)