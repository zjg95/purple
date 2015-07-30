from __future__ import division
from PlayingCards import Card, Deck

def guessBlack(deck) :
	return deck.nextCard().black()

def guessRed(deck) :
	return deck.nextCard().red()

def guessPurple(deck) :
	return False #to be updated	

def guess(color, deck) :
	if color == 'r' :
		return guessRed(deck)
	if color == 'b' :
		return guessBlack(deck)
	return guessPurple(deck)

deck = Deck()
print("Red:")
success = 0
failure = 0
for i in range(0, 52) :
	result = guess('r', deck)
	if result == True :
		success += 1
	else :
		failure += 1
print(success)
print(failure)
print(str(success / 52) + "% success, " + str(failure / 52) + "% failure")

print(" ")
deck = Deck()
print("Black:")
success = 0
failure = 0
for i in range(0, 52) :
	result = guess('b', deck)
	if result == True :
		success += 1
	else :
		failure += 1
print(success)
print(failure)
print(str(success / 52) + "% success, " + str(failure / 52) + "% failure")

print(" ")
deck = Deck()
print("Purple:")
success = 0
failure = 0
for i in range(0, 26) :
	result = guess('p', deck)
	if result == True :
		success += 1
	else :
		failure += 1
print(success)
print(failure)
print(str(success / 26) + "% success, " + str(failure / 26) + "% failure")

