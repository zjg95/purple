from __future__ import division
from PlayingCards import Card, Deck
import random

def percent(piece, total) :
	return str((piece / total) * 100)

def guessBlack(deck) :
	return deck.nextCard().black()

def guessRed(deck) :
	return deck.nextCard().red()

def guessPurple(deck) :
	c1 = deck.nextCard()
	c2 = deck.nextCard()
	return (c1.black() and c2.red()) or (c1.red() and c2.black())	

def guess(color, deck) :
	if color == 'r' :
		return guessRed(deck)
	if color == 'b' :
		return guessBlack(deck)
	return guessPurple(deck)

guesses = ['r','b','p']

for i in range(0,3) :
	print(guesses[i] + ":")
	success = 0
	failure = 0
	trials  = 0
	for n in range(0, 100) :
		deck = Deck()
		try :
			while True :
				result = guess(guesses[i], deck)
				if result == True :
					success += 1
				else :
					failure += 1
				trials += 1
		except :
			pass
	print(success)
	print(failure)
	print(percent(success, trials) + "% success")
	print(percent(failure, trials) + "% failure")
	print(" ")

success = {'r' : 0, 'b' : 0, 'p': 0}
failure = {'r' : 0, 'b' : 0, 'p': 0}
trials  = 0
for n in range(0, 100) :
	deck = Deck()
	try :
		while True :
			pick = random.choice(guesses)
			print(pick)
			result = guess(pick, deck)
			print(result)
			trials += 1
			print(trials)
			if result == True :
				success[guess] += 1
			else :
				failure[guess] += 1
	except :
		pass

assert trials > 0

print("red:")
print(percent(success['r'], trials) + "% success")
print(percent(failure['r'], trials) + "% failure")
print("black:")
print(percent(success['b'], trials) + "% success")
print(percent(failure['b'], trials) + "% failure")
print("purple:")
print(percent(success['p'], trials) + "% success")
print(percent(failure['p'], trials) + "% failure")
