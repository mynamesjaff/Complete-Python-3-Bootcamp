''' 
Blackjack project
Create a deck of 52 cards
Shuffle the deck
Ask the Player for their bet
Make sure that the Player's bet does not exceed their available chips
Deal two cards to the Dealer and two cards to the Player
Show only one of the Dealer's cards, the other remains hidden
Show both of the Player's cards
Ask the Player if they wish to Hit, and take another card
If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
Determine the winner and adjust the Player's chips accordingly
Ask the Player if they'd like to play again

A standard deck of playing cards has four suits (Hearts, Diamonds, Spades and Clubs) and 
thirteen ranks (2 through 10, then the face cards Jack, Queen, King and Ace) for a total of
52 cards per deck. Jacks, Queens and Kings all have a rank of 10. Aces have a rank of either 
11 or 1 as needed to reach 21 without busting. As a starting point in your program, you may
want to assign variables to store a list of suits, ranks, and then use a dictionary to map 
ranks to values.
'''

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return "%s of %s" %(self.rank, self.suit) 
		#alternative - return "{} of {}".format(self.rank, self.suit) 
		#alternative - return f'{self.rank} of {self.suit}'

class Deck:
	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))
	def __str__(self): #makes it possible to print the instance of the class (test_deck)
		deck_composition = " "
		for card in self.deck:
			deck_composition += card.__str__() + "\n"
		return f"The deck has :{deck_composition}"

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		return self.deck.pop()

class Hand:
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0 

	def __str__(self):
		hand_composition = ""
		for card in self.cards:
			hand_composition += card.__str__() + ", "
		return hand_composition

	def add_card(self,card):
		self.cards.append(card)
		if card.rank == "Ace":
			self.aces += 1
		self.value += values.get(card.rank)
		return self.value

	def adjust_for_ace(self):
		if self.value > 21 and self.aces >= 1:
			self.value -= 10
			self.aces -= 1


class Chips:
	def __init__(self):
		self.total = 100 
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet


def take_bet(chips):
	while True:
		try:
			bet = int(input("Please place your bet: "))
			while bet > player_chips.total:
				print("That bet exceeds your current available chips")
				bet = int(input("Please place your bet: "))
		except:  #will run if you have an error
			print("Not a valid bet, please enter a number.")
			continue
		else:
			chips.bet = bet
			break
			#break - don't need because return breaks out of method

#player_bet = take_bet()
#print(player_bet)

def hit(deck,hand):
	pop_card = deck.deal()
	hit_card_value = hand.add_card(pop_card)
	hand.adjust_for_ace()
	#print(hit_card_value)
	#print(hand.value)

def hit_or_stand(deck,hand):
	global hitting # to control an upcoming while loop
	h_or_s = 'x'
	while h_or_s != 'h' and h_or_s != 's':
		h_or_s = input("Would you like to hit or stand? Press 'h' for hit, or 's' for stand: ").lower()	
	if h_or_s == 'h':
		hit(deck,hand)
	elif h_or_s == 's':
		hitting = False

def show_some(player,dealer):
	player_string = ""
	dealer_string = ""
	for card in dealer.cards[1::]:
		 dealer_string +=  card.__str__() + " "
	for card in player.cards:
		player_string +=  card.__str__() + " "
	print("----------------------------------------------------------------------")
	print(f"\nThe dealer hand contains\nFace down card {dealer_string}\n")
	print(f"The player hand contains\n{player_string}\nPlayer value: {player.value}\n")
	print("----------------------------------------------------------------------")
#show_some(player_hand,dealer_hand)

def show_all(player,dealer):
	player_string = ""
	dealer_string = ""
	for card in dealer.cards:
		dealer_string +=  card.__str__() + " "
	for card in player.cards:
		player_string +=  card.__str__() + " "
	print("----------------------------------------------------------------------")
	print(f"The dealer hand contains\n{dealer_string}Dealer value: {dealer.value}\n")
	print(f"The player hand contains\n{player_string}\nPlayer value: {player.value}\n")
	print("----------------------------------------------------------------------")
#show_all(player_hand,dealer_hand)

def player_busts(chips):
	chips.lose_bet()
	print(f"You busted!\nYour total chip count is now {chips.total}")

def player_wins(chips):
	chips.win_bet()
	print(f"You win!\nYour total chip count is now {chips.total}")

def dealer_busts(chips):
	chips.win_bet()
	print(f"The dealer busted!\nYour total chip count is now {chips.total}")

def dealer_wins(chips):
	chips.lose_bet()
	print(f"The dealer wins!\nYour total chip count is now {chips.total}")

def push(chips):
	print(f"It's a push!\n Your total chip count stays at {chips.total}")

def replay():
	play_again = input("Would you like to play again?\n 'Y' for yes, 'N' for no: ").upper()
	while play_again != 'Y' and play_again != 'N':
		print("Dude you gotta press Y or N")
		play_again = input("Would you like to play again?\n 'Y' for yes, 'N' for no: ").upper()
	return play_again == 'Y'

def if_21(player,dealer):
	global playing
	global hitting
	if player.value == 21:
		while dealer.value < 17:
			hit(blackjack_deck,dealer_hand)
		if dealer.value > 21:
			dealer_busts(player_chips)
			playing = False
			hitting = False
		elif player.value == dealer.value:
				push()
		else:
			player_wins(player_chips)
			playing = False
			hitting = False


player_chips = Chips() #have to create this outside of while loop in order to not reset the counter to 100
print("Welcome to Blackjack!")
while True:
	blackjack_deck = Deck()
	blackjack_deck.shuffle()
	print(f"Your current chip value is {player_chips.total}")
	player_bet = take_bet(player_chips)
	player_hand = Hand()
	dealer_hand = Hand()
	hit(blackjack_deck, dealer_hand) #initial deal
	hit(blackjack_deck, player_hand) #initial deal
	hit(blackjack_deck, dealer_hand) #initial deal
	hit(blackjack_deck, player_hand) #initial deal
	show_some(player_hand,dealer_hand)
	playing = True
	hitting = True
	while playing:
		if_21(player_hand,dealer_hand)
		while hitting:
			hit_or_stand(blackjack_deck, player_hand)
			show_some(player_hand, dealer_hand)
			if_21(player_hand,dealer_hand)
			if player_hand.value > 21:
				player_busts(player_chips)
				playing = False
				break
		if player_hand.value <= 21:
			while dealer_hand.value < 17:
				hit(blackjack_deck,dealer_hand)
			if dealer_hand.value > 21:
				show_all(player_hand, dealer_hand)
				dealer_busts(player_chips)
				playing = False
				break
		#show_all(player_hand,dealer_hand)
		if player_hand.value <= 21 and player_hand.value > dealer_hand.value:
			show_all(player_hand,dealer_hand)
			player_wins(player_chips)
			break
		elif dealer_hand.value <= 21 and dealer_hand.value > player_hand.value:
			show_all(player_hand,dealer_hand)
			dealer_wins(player_chips)
			break
		elif dealer_hand.value == player_hand.value:
			show_all(player_hand,dealer_hand)
			push(player_chips)
			break
	if player_chips.total == 0:
		print("You're all out of chips! Game over!")
		break
	if not replay():
		break
print("Thanks for playing!")



