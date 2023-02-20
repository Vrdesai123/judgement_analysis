from game_logic import Judgement

if __name__ == '__main__':
    Instance = Judgement(4)
    Instance.deal(2, 10)
    print(Instance.hand_dist)
        
    