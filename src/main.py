from game_logic import Judgement

if __name__ == '__main__':
    Instance = Judgement(4)
    Instance.assign_player_hands()
    Instance.take_turn()
        
    