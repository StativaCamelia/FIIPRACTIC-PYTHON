RANKS = {'2' : 2, '3' : 3, '4' : 4, '5' : 5, '6': 6, '7': 7, '8': 8, '9':9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
SUITS = {'S' : 1, 'H' : 2, 'D' : 3, 'C': 4}


class Card:
	def __init__(self, rank, suit, up=False):
		self.up = up
		self.rank = rank
		self.suit = suit

	@property
	def rank(self):
		return self._rank

	@property
	def suit(self):
		return self._suit

	@rank.setter
	def rank(self, rank):
		if rank in RANKS:
			self._rank = rank

	@suit.setter
	def suit(self, suit):
		if suit in SUITS:
			self._suit = suit

	def __eq__(self, other):
		return RANKS[self._rank] == RANKS[other.rank]

	def __gt__(self, other):
		return RANKS[self._rank] > RANKS[other.rank]

	def __str__(self):
		return "Rank: " + str(self._rank) + " Suit:" + str(self._suit)