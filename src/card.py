class Card:

    def __init__(self, rank: int, suit: str):
        """
        desc: Class which defines each individual card in the deck with its two properties, suit and rank  
        
        inputs (init_constructor): 
        - rank -> int: an integer indicating the value hierarchy of the card with 2 being the lowest and \
            Ace the highest.
        - suit -> str: a string describing what suit the card is out out of Hears, Spades, Clubs, Diamonds

        methods:
        - display_card() -> NoneType

        """
        self.suit = suit
        self.rank = rank
        self.card_name = f"{self.rank} of {self.suit}"

    def display_card(self):
        """
        desc: prints the card name in an understandable way
        """

        print(self.card_name)
