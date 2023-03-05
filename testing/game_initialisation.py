import unittest
import logging
import sys
from src.game_logic import Judgement

class Deal_Checker(unittest.TestCase):
    # change name of these unittests to reflect utility
    def testSomething(self):
        self.Game = Judgement(2)
        self.Game.assign_player_hands()
        log = logging.getLogger("Deal_Checker.testSomething")
        log.debug("Shuffled list %r", self.Game.player_hands)

    # create follow up tests for assigning and guessing tricks
    def assign_tricks(self):
        self.Game.guess_player_tricks()
        # Pass inputs to this

        
if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("Deal_Checker.testSomething").setLevel(logging.DEBUG)
    unittest.main()       