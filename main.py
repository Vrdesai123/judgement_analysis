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
        super().__init__(suits=suits, ranks=ranks)
        self.n_players = n_players
        self.total_rounds = 52 // self.n_players
        self.trumps = ranks + ["No Trump"]

    def deal(self, round = 1):
        Judgement.shuffle_deck()
        self.round = round
        self.trump_state = self.trumps[(self.round - 1) % 5]
        
        #index slicing for dealing
        

        


Judgement()


