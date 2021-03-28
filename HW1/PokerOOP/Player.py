types = ["button", "small blind", "big blind"]

class Player:
	def __init__(self, name):
		self.name = name
		self.cards = ""
		self.type = type

	def __str__(self):
		return self.name

	@property
	def cards(self):
		return self._cards

	@cards.setter
	def cards(self, cards):
		self._cards = cards

	@property
	def type(self):
		return self._type

	@type.setter
	def type(self, type):
		self._type = type

	def __eq__(self, other):
		return self.name == other.name