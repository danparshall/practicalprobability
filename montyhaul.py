import numpy as np


class trial(object):

	# prize is randomly assigned
	def __init__(self):
		self.prize = np.random.randint(0,3)


	# user chooses a door to bet on
	def makeBet(self,bet):
		assert isinstance(bet,int)
		assert bet <= 2
		assert bet >= 0
		self.bet = bet


	# monty opens one door to reveal a booby prize
	def openDoor(self):
		doors = np.array([0,0,0])
		doors[self.prize] = 1
		doors[self.bet] = 1

		# monty's choice is between two doors (if user is selecting prize), or
		# restricted to single door if users door and prize door are different
		freeDoors = np.where(doors==0)[0]
		montyDoor = freeDoors[np.random.randint(len(freeDoors))] # door index
		self.montyDoor = montyDoor

		# value behind the montyDoor should always be zero
		if doors[montyDoor]:
			print "THAT WAS SUPPOSED TO BE ZERO :( "
		return montyDoor


	# user may choose to change their bet to the remaining closed door
	def changeDoor(self,change=False):
		doors = np.array([0,0,0])
		doors[self.montyDoor] = 1
		doors[self.bet] = 1

		option = np.where(doors==0)[0]

		if change:
			self.bet = option


	# If prize is behind user's bet, it's a winner
	def resolve(self):
		if self.bet == self.prize:
			return 1
		else:
			return 0


wins = 0
runs = 10000
for i in range(runs):
	ordeal = trial()
	ordeal.makeBet(np.random.randint(3))
	opened = ordeal.openDoor()
	ordeal.changeDoor(True)
	wins += ordeal.resolve()

print wins*1.0/runs
