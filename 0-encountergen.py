# Dungeon Area / Encounter Gen
# Parameters: none
# Encounter builder is based on a deck of cards drawing from the deck to build a series of encounters.
# 2 - 5 represent groups of minion monsters
# 6 - 9: 1 to 1
# 10/Jack: 2 to 1
# Queen: 3 to 1
# King: 4 to 1
# Ace: 5 to 1, when the 4th Ace is drawn all other cards are discarded as this becomes a solo monster encounter

# The suits
# Spades & Clubs are the primary monsters
# Hearts represent ally and guardian monsters.
# Diamonds repesent subservant monsters except when a face card diamond is the highest card.
# 	When this occurs the other cards are discarded and the difficulty is increased by 1 for the lone monster, usually some sort of lurker.

# Import
import random

# List
spades = ["1:12 Primary/Sub", "1:8 Primary/Sub", "1:4 Primary/Sub", "1:2 Primary/Sub", "1:1 Primary", "1:1 Primary", "1:1 Primary", "1:1 Primary", "2:1 Primary", "2:1 Primary", "3:1 Primary", "4:1 Primary", "ACE | 5:1 Primary"]
clubs = ["1:12 Primary/Sub", "1:8 Primary/Sub", "1:4 Primary/Sub", "1:2 Primary/Sub", "1:1 Primary", "1:1 Primary", "1:1 Primary", "1:1 Primary", "2:1 Primary", "2:1 Primary", "3:1 Primary", "4:1 Primary", "ACE | 5:1 Primary"]
hearts = ["1:12 Ally/Guardian", "1:8 Ally/Guardian", "1:4 Ally/Guardian", "1:2 Ally/Guardian", "1:1 Ally/Guardian", "1:1 Ally/Guardian", "1:1 Ally/Guardian", "1:1 Ally/Guardian", "2:1 Ally/Guardian", "2:1 Ally/Guardian", "3:1 Ally/Guardian", "4:1 Ally/Guardian", "ACE | 5:1 Ally/Guardian"]
diamonds = ["1:12 Sub", "1:8 Sub", "1:4 Sub", "1:2 Sub", "1:1 Sub", "1:1 Sub", "1:1 Sub", "1:1 Sub", "5:1 or 3:1 x2 Lone/Pair", "5:1 or 3:1 x2 Lone/Pair", "5:1 or 3:1 x2 Lone/Pair", "5:1 or 3:1 x2 Lone/Pair", "ACE | 6:1 or 4:1 x2 Lone/Pair"]

deck = spades + clubs + hearts + diamonds
random.shuffle(deck)

ace = "ACE"
lone = "Lone"
a = 0
d = 0
e = (random.randint(1, 3) + random.randint(1, 3)) + 1

while e > 0:
	print("Encounter")
	c = (random.randint(1, 3) + random.randint(1, 3)) + 1
	l = 0
	while c > 0:
		print(deck[d])
		if ace in deck[d]:
			a += 1
			if a == 4: print("4th Ace - Solo Encounter, discard all other cards")
		elif lone in deck[d]: l = 1 
		d += 1
		c -= 1
	if l == 1:
		print("If the Lone Monster exceeds the difficulty of the other monsters discard the other monsters otherwise discard the lone monster")
	e -= 1
	print("")
