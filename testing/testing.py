import unittest
import logging
import sys
from src import card
from src.game_logic import Deck

class SomeTest(unittest.TestCase):
    # change name of these unittests to reflect utility
    def testSomething(self):
        Deck_state = Deck()
        dealt_list = Deck_state.deal(3,10)
        log = logging.getLogger("SomeTest.testSomething")
        log.debug("Shuffled list %r", dealt_list)
        log.debug("total cards dealt = %r", dealt_list.size)
        
if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("SomeTest.testSomething").setLevel(logging.DEBUG)
    unittest.main()       