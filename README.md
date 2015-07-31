# purple

Purple is a card game invented by a friend of mine. It is played with a regular deck of playing cards.
The objective is to guess the color of the next card that comes from the deck. Red for red, black for black, and purple for opposite colors (2 cards). If the next two cards are red and black, or black and red, purple succeeds.

While the probability of guessing black or red is expected to be 50%, the probability of drawing purple is unclear. Intuitively it would seem that the probability would be 25% since you are working with two cards, but since the order does not matter, the chances are actually raised.

To prove this, I wrote a quick program in python to model this game, and see the results. Interestingly enough, the probability of purple succeeding fluctuates between 47%-68%. Over the course of several trials though, this average converges to somewhere around 52%, which is higher than red/black which consistently stay at 50%. 

This surprisingly proves that the probability of purple succeeding is greater than red or black.
