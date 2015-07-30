from PlayingCards import Card, Deck

def guessBlack(deck) :
	return deck.nextCard().red()

def guessRed(deck) :
	return deck.nextCard().black()

def guess(color, deck) :
	if color == 'r' :
		return guessRed(deck)
	if color == 'b' :
		return guessBlack(deck)
	return guessPurple(deck)

deck = Deck()
print("guessing red")
true  = 0
false = 0
for i in range(0, 52) :
	result = guess('r', deck)
	print(" " + str(result))
	if result :
		true += 1
	else :
		false += 1
