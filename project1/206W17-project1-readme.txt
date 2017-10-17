206 Project 1 - Code for playing cards
README

Your name: Chalse Okorom
Anyone you worked with:

----- Add your README file content for the Project 1 code.

This code allows the user to simulate a card game with two players, using the function play_war_game(). Each player has a shuffled deck. Then, both players remove a card from their deck to compare them. The player with he highest ranking card gets a point. The players keep comparing cards until they both run out of cards in their decks. The player with the highest score at the end of the rounds is declared the winner. It was written to simulate an automated instance of the game War.

There are three classes in this code:

1. The Card class allows us to create a representation of a playing card using two required parameters -- an integer corresponding to a suit and a an integer corresponding to a rank.

	The __init__() method of the Card class is a constructor requiring two integer inputs that allow the user to set the suit and rank of a Card.

	The __str__() method of the Card class doesn't require any inputs. It allows the user to output out the value of a card in the format "<rank> of <suit>"

2. The Deck class allows us to create a representation of a deck of playing cards, serving as a class containing a list of fifty-two distinct cards that can be manipulated using the various methods of this class. There is no input required for this class.
	
	The __init__() method of the Deck class initializes an instance of the class and requires no input, appending Card instances to <cards> in a sorted order.

	The __str__() method of the Deck class requires no input, returning a multi-line string that lists each card in cards.

	The pop_card() method of the Deck class requires no input. It removes the last card in the deck by default and returns it. If you use the optional integer parameter, you can choose a specific card to be removed from <cards> and return it.

	The shuffle() method of the Deck class requires no input. It rearranges the order of the Cards instances in <cards> of the Deck class.

	The replace_card() method of the Deck class requires the input of a Card.It looks for an instance of that Card in the <card_strs> and adds it to <cards> if it is not already there.

	The sort_cards() method of the Deck class does not require any inputs. It empties <cards> and remakes it in a sorted way.

3. The Hand class allows us to make a representation of a hand of cards for the games, including the basic functionality of the number of cards attribute.
	
	The __init__() method of the Hand class is a constructor that has two parameters -- <deck_to_use> and <num_cards>. <num_cards> is an optional integer parameter, that is set to a default of 5 cards, while <deck_to_use> is a required Deck parameter. This method appends <num_cards> Cards from the the Deck to <cards_in_hand>.

	The place_card() method of the Hand class requires no input. By default, it removes the last card in the Hand and returns it. If you use the optional integer paremeter, you can choose a specific card from the Hand to be removed and returned. 

	The get_suits_available() method of the Hand class requires no input. It returns a list of all the suits that are in the hand.

	The get_ranks_available() method of the Hand class requires no input. It returns a list of all the ranks that are in the hand.

	The specific_card() method of the Hand class requires an input of suit and rank. It will then check whether a card with both of those parameters is in the hand. If it is, then that card is removed from the Hand and returned in this method. Otherwise, if there is no such card in the hand, nothing will be removed from the hand.

	The add_card() method of the Hand class requires one Card parameter. It makes a list of strings representing cards in the Hand. Then, it checks if any of them match the Card parameter input into this method. If it isn't in the list, then, the Card parameter input is appended to <cards_in_hand>.

	The __str__() method of the Hand class requires no input. It returns a multi-line string listing each card in whatever order the cards are in.