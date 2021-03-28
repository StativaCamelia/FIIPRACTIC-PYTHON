from PokerOOP.Player import Player
from PokerOOP.Table import Table
from PokerOOP.Utils.Exceptions import NotEnoughPlayers, Conflict, NoSuchPlayer


class Game:
	def __init__(self):
		self.players = []
		self.number_of_players = 0
		self.deck = None
		self.table = Table()

	def get_number_of_players(self):
		print('Enter the number of players:')
		self.number_of_players = int(input())
		if self.number_of_players < 2:
			raise NotEnoughPlayers()

	def set_players(self):
		for _ in range(self.number_of_players):
			print('Enter player name:')
			name = input()
			if name in self.get_players():
				raise Conflict(name)
			self.players.append(Player(name))

	def select_dealer(self):
		print('Enter the name of the dealer')
		name = input()
		if name not in self.get_players():
			raise NoSuchPlayer(name)

	def print_players(self):
		for player in self.players:
			print(player)


	def get_players(self):
		return list(map(lambda x: x.name, self.players))

	def print_table(self):
		self.table.print_cards_on_table()
