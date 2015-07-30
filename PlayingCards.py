import random

class Card :

	def __init__(self, number, color, suite) :
		self.number = number
		self.color  = color
		self.suite  = suite

	def __str__(self) :
		return str(self.number) + str(self.suite)
	
	def black(self) :
		return self.color == 'b'

	def red(self) :
		return self.color == 'r'

class Deck :
	def __init__(self) :
		self.master = []
		for i in [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] :
			self.master += [Card(i, 'b', 's')]
			self.master += [Card(i, 'b', 'c')]
			self.master += [Card(i, 'r', 'h')]
			self.master += [Card(i, 'r', 'd')]
		self.shuffle()

	def nextCard(self) :
		if len(self.cards) == 0 :
			raise IndexError
		card = self.cards[0]
		self.cards.pop(0)
		return card

	def shuffle(self) :
		copy = self.master
		self.cards = []
		for i in range(0, 52) :
			card = random.choice(copy)
			copy.remove(card)
			self.cards += [card]
		assert len(self.cards) == 52
		assert len(copy) == 0

	def __iter__(self) :
		return iter(self.cards)

	def __len__(self) :
		return len(self.cards)
