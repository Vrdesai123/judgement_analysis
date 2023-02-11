import pandas as pd
import numpy as np
import random 

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

class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def display_card(self):
        print(f"{self.rank} of {self.suit}")




class Deck():
    def __init__(self, suits, ranks):

        self.order = []
        self.suits = suits
        self.ranks = ranks
        for st in self.suits:
            for rk in ranks.keys():
                self.order.append(Card(rk, st))

        random.shuffle(self.order)

    def shuffle_deck(self):
        random.shuffle(self.order)
    

                    
class Judgement(Deck):
    def __init__(self, n_players):
        self.deck_state = super().__init__(suits=suits, ranks=ranks)
        self.n_players = n_players
        self.total_rounds = 52 // self.n_players
        self.trumps = suits + ["No Trump"]

    def deal(self, round):
        self.round = round
        self.trump_state = self.trumps[(self.round - 1) % 5]
        self.cards_dealt = 52 // self.n_players - (self.n_players * (round - 1))

        #index slicing for dealing
        self.hand_dist = np.empty(self.n_players)
        for n in range(self.n_players):
            self.hand_dist = np.append(self.hand_dist, self.order[:self.n_players], axis=0)
            self.order = self.order[self.n_players:]

        return self.hand_dist
        

         

        





