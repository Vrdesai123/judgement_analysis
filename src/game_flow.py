from game_logic import Judgement

n_players = 4

Game_Instance = Judgement(n_players)
while Game_Instance.round <= Game_Instance.total_rounds:
    Game_Instance.assign_player_hands()
    Game_Instance.guess_player_tricks()

    while Game_Instance.turn <= Game_Instance.n_cards_dealt:
        Game_Instance.take_turn()
        Game_Instance.turn_evaluator()

    
    Game_Instance.round_evaluator()


    
        