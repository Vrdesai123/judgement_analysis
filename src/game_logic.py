import numpy as np
import random 
import string
import sys
import pandas as pd

from src.card import Card
from src.deck import Deck
   

                    
class Judgement(Deck):
    def __init__(self, n_players: int):
        """
        desc: a child class of Deck, it manipulates the Deck object and plays the game of judgement
            with all game state information contained
        
        inputs:
        - n_players -> int: specifies the number of players in the game

        method:

        """
        
        # game information
        super().__init__()
        self.n_players = n_players
        self.total_rounds = 52 // self.n_players
        self.trumps = self.suits + ["No Trump"]
        self.player_names = [''.join(random.choices(string.ascii_lowercase, k=5)) \
            for n in range(self.n_players)]
        self.hand_dist = None

        # game state information
        self.round = 1
        self.turn = 1
        self.trump_state = self.trumps[(self.round - 1) % 5]

        self.cards_played_outofplay = []

    def assign_player_hands(self):
            self.shuffle_deck()
            self.hand_dist = self.deal(self.n_players, self.round)
            self.player_hands = pd.DataFrame(data = self.hand_dist, columns = self.player_names)
            self.round_history = []
    
    def guess_player_tricks(self):

        self.player_tricks = []

        for player in self.player_names:
            print("Guess the number of tricks you will win")
            print(self.translate_cards(self.player_hands[player]))
            while True:
                    try:
                        choice = int(input())

                        if choice > self.n_cards_dealt:
                            print("Guess is too high!")
                            raise ValueError
                        
                        elif choice < 0:
                            print("Guess is too low")
                            raise ValueError
                        
                        elif self.player_names.index(player) == (self.n_players - 1) \
                            and (self.n_cards_dealt - sum(self.player_tricks) - choice) == 0:

                            print(f"Guess cannot be {choice} for the last player {player}")
                            raise ValueError
                        break
                    except:
                        print("choose a valid guess ")
            self.player_tricks.append()
            
    
    def take_turn(self):
        """
        Take an input from each player and save the card they played, pass it to an evaluator function
        and count up the turn by 1 
        """

        self.played = []

        for player in self.player_names:
            print(self.translate_cards(self.player_hands[player]))
            print([i for i in range(len(self.player_hands[player]))])
            
            while True:
                try:
                    choice = int(input())
                    break
                except:
                    print("choose an index as displayed")

            self.played.append(list(self.player_hands[player]).pop(choice))            

    def turn_evaluator(self):
        
        ###

        self.turn += 1
        self.round_history += self.played

    def round_evaluator(self):
        pass

        

    

   

        

 


