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


	# Monty opens one door to reveal a booby prize
	def openDoor(self):
		doors = np.array([0,0,0])
		doors[self.prize] = 1
		doors[self.bet] = 1

		# Monty's choice is between two doors (if user is selecting prize), or
		# restricted to single door if user's door and prize door are different
		freeDoors = np.where(doors==0)[0]
		MontyDoor = freeDoors[np.random.randint(len(freeDoors))] # door index
		self.MontyDoor = MontyDoor

		# value behind the MontyDoor should always be zero
		if doors[MontyDoor]:
			print "THAT WAS SUPPOSED TO BE ZERO :( "
		return MontyDoor


	# user may choose to change their bet to the remaining closed door
	def changeDoor(self,change=False):
		doors = np.array([0,0,0])
		doors[self.MontyDoor] = 1
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


def runOrdeals(runs,changeDoor):
	wins = 0
	for i in range(runs):
		ordeal = trial()
		ordeal.makeBet(np.random.randint(3))
		opened = ordeal.openDoor()
		ordeal.changeDoor(changeDoor)
		wins += ordeal.resolve()
	return wins


runs = 10000
winChange = runOrdeals(runs,True)
winKeep = runOrdeals(runs,False)

print "When Keeping the original door, win probability is", winKeep*1.0/runs
print "When Changing the original door, win probability is", winChange*1.0/runs
