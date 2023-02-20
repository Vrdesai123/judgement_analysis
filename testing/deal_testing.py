import unittest
import logging
import sys
from src.game_logic import Judgement

class Deal_Checker(unittest.TestCase):
    # change name of these unittests to reflect utility
    def testSomething(self):
        Game = Judgement(2)
        dealt_list = Game.assign_player_hands()
        log = logging.getLogger("Deal_Checker.testSomething")
        log.debug("Shuffled list %r", dealt_list)

        
if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("Deal_Checker.testSomething").setLevel(logging.DEBUG)
    unittest.main()       