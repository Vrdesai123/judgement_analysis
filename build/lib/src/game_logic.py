import numpy as np
import random 
import sys
from src.card import Card


ranks = {"Ace": 14,
        "Two": 2,

        "Three": 3,
        "Four": 4,
        "Five": 5,
        "Six": 6,
        "Seven": 7,
        "Eight": 8,
        "Nine": 9,
        "Ten": 10,
        "Jack": 11,
        "Queen": 12,
        "King": 13}

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]


class Deck:
    def __init__(self, suits: list = suits, ranks: dict = ranks):
        """
        desc: this class creates a full 52-card deck iteratively with the ability to shuffle the deck

        inputs: 
        - suits -> list: a list of the possible suits, this should always be the default provided.
            Changing the order of the list will affect the order of the trump suit in the rounds
        - ranks -> dict: a dictionary of the names of the cards keyed to the values they hold in
            the game of judgement

        methods:
        - shuffle_deck() -> NoneType
        """
        self.order = []
        self.suits = suits
        self.ranks = ranks
        for st in self.suits:
            for rk in ranks.keys():
                self.order.append(Card(rk, st))

        random.shuffle(self.order)

    def shuffle_deck(self):
        """
        desc: shuffles the deck order provided with a list shuffle
        """
        random.shuffle(self.order)
    
    def deal(self, n_players: int, round: int = 1) -> np.array:
        """
        desc: a method of Deck class which evenly deals out the cards in the deck

        inputs:
        - n_players -> int: the number of players playing which must be in [2,52]
        - round -> int: an indicator of which round we are playing, note the max number of rounds
            is limited by n_max = 52 // n_players
        
        outputs:
        - hand_dist -> np.array: this is a representation of the construction of each player's hand
            with shape (n_players, cards_dealt)
        """

        #create proper error messages
        if n_players not in range(2,53):
            print("too many players") 
            sys.exit()

        if round > 52 // n_players:
            print("too high round number specified")
            sys.exit()

        self.n_players = n_players
        self.round = round
        self.cards_dealt = (52 - (self.n_players * (round - 1))) // self.n_players 

        #index slicing for dealing
        self.hand_dist = np.empty((0,0), Card)
        for n in range(self.n_players):
            self.hand_dist = np.append(self.hand_dist, self.order[:self.cards_dealt], axis=None)
            self.order = self.order[self.cards_dealt:]

        # not ideal, should append with correct dimensionality
        self.hand_dist = self.hand_dist.reshape(self.n_players,self.cards_dealt)
        return self.hand_dist

    def translate_cards(self):
        """
        desc: transforms card object to a more readable format, may deprecate soon
        """
        return [i.card_name for i in self.hand_dist]
        
    

                    
class Judgement(Deck):
    def __init__(self, n_players: int):
        """
        desc: a child class of Deck, it manipulates the Deck object and plays the game of judgement
            with all game state information contained
        
        inputs:
        - n_players -> int: specifies the number of players in the game

        methods:
        - deal() -> np.array

        """
        self.deck_state = super().__init__(suits=suits, ranks=ranks)
        self.n_players = n_players
        self.total_rounds = 52 // self.n_players
        self.trumps = suits + ["No Trump"]
        self.trump_state = self.trumps[(self.round - 1) % 5]

    

   

        




