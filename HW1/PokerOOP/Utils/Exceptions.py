class NotEnoughPlayers(Exception):
	def __init__(self, message = "There must be at least 4 players to play the game"):
		self.message = message
		super().__init__(self.message)

class Conflict(Exception):
	def __init__(self, player_name):
		self.name = player_name

	def __str__(self):
		return f"The player {self.name} already exists"

class NoSuchPlayer(Exception):
	def __init__(self, player_name):
		self.name = player_name

	def __str__(self):
		return f"The player {self.name} does not  exists"

