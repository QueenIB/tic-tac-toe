class TicTacToe:
    def __init__(self):
        self.player_1_score = 0
        self.player_2_score = 0

    def win_condition(self, player_1, player_2, game):
        lines = game.split('\n')
        game_over = True
        if lines[0][2] == lines[0][8] == lines[0][14] == player_1:
            print("\nGame Over!\nPlayer 1 Wins!")
            self.player_1_score += 1
            print(f"Player 1 score: {self.player_1_score}\nPlayer 2 "
                  f"score: {self.player_2_score}")
            return game_over
        elif lines[0][2] == lines[0][8] == lines[0][14] == player_2:
            print("\nGame Over!\nPlayer 2 Wins!")
            self.player_2_score += 1
            print(f"Player 1 score: {self.player_1_score}\nPlayer 2 "
                  f"score: {self.player_2_score}")
            return game_over
        elif lines[2][2] == lines[2][8] == lines[2][14] == player_1:
            print("\nGame Over!\nPlayer 1 Wins!")
            self.player_1_score += 1
            print(f"Player 1 score: {self.player_1_score}\nPlayer 2 "
                  f"score: {self.player_2_score}")
            return game_over
        elif lines[2][2] == lines[2][8] == lines[2][14] == player_2:
            print("\nGame Over!\nPlayer 2 Wins!")
            self.player_2_score += 1
            print(f"Player 1 score: {self.player_1_score}\nPlayer 2 "
                  f"score: {self.player_2_score}")
            return game_over
        elif lines[4][2] == lines[4][8] == lines[4][14] == player_1:
            print("\nGame Over!\nPlayer 1 Wins!")
            self.player_1_score += 1
            print(f"Player 1 score: {self.player_1_score}\nPlayer 2 "
                  f"score: {self.player_2_score}")
            return game_over
        elif lines[4][2] == lines[4][8] == lines[4][14] == player_2:
            print("\nGame Over!\nPlayer 2 Wins!")
            self.player_2_score += 1
            print(f"Player 1 score: {self.player_1_score}\nPlayer 2 "
                  f"score: {self.player_2_score}")
            return game_over
        elif lines[0][2] == lines[2][8] == lines[4][14] == player_1:
            print("\nGame Over!\nPlayer 1 Wins!")
            self.player_1_score += 1
            print(f"Player 1 score: {self.player_1_score}\nPlayer 2 "
                  f"score: {self.player_2_score}")
            return game_over
        elif lines[0][2] == lines[2][8] == lines[4][14] == player_2:
            print("\nGame Over!\nPlayer 2 Wins!")
            self.player_2_score += 1
            print(f"Player 1 score: {self.player_1_score}\nPlayer 2 "
                  f"score: {self.player_2_score}")
            return game_over
        elif lines[0][14] == lines[2][8] == lines[4][2] == player_1:
            print("\nGame Over!\nPlayer 1 Wins!")
            self.player_1_score += 1
            print(f"Player 1 score: {self.player_1_score}\nPlayer 2 "
                  f"score: {self.player_2_score}")
            return game_over
        elif lines[0][14] == lines[2][8] == lines[4][2] == player_2:
            print("\nGame Over!\nPlayer 2 Wins!")
            self.player_2_score += 1
            print(f"Player 1 score: {self.player_1_score}\nPlayer 2 "
                  f"score: {self.player_2_score}")
            return game_over
        elif lines[0][2] == lines[2][2] == lines[4][2] == player_1:
            print("\nGame Over!\nPlayer 1 Wins!")
            self.player_1_score += 1
            print(f"Player 1 score: {self.player_1_score}\nPlayer 2 "
                  f"score: {self.player_2_score}")
            return game_over
        elif lines[0][2] == lines[2][2] == lines[4][2] == player_2:
            print("\nGame Over!\nPlayer 2 Wins!")
            self.player_2_score += 1
            print(f"Player 1 score: {self.player_1_score}\nPlayer 2 "
                  f"score: {self.player_2_score}")
            return game_over
        elif lines[0][8] == lines[2][8] == lines[4][8] == player_1:
            print("\nGame Over!\nPlayer 1 Wins!")
            self.player_1_score += 1
            print(f"Player 1 score: {self.player_1_score}\nPlayer 2 "
                  f"score: {self.player_2_score}")
            return game_over
        elif lines[0][8] == lines[2][8] == lines[4][8] == player_2:
            print("\nGame Over!\nPlayer 2 Wins!")
            self.player_2_score += 1
            print(f"Player 1 score: {self.player_1_score}\nPlayer 2 "
                  f"score: {self.player_2_score}")
            return game_over
        elif lines[0][14] == lines[2][14] == lines[4][14] == player_1:
            print("\nGame Over!\nPlayer 1 Wins!")
            self.player_1_score += 1
            print(f"Player 1 score: {self.player_1_score}\nPlayer 2 "
                  f"score: {self.player_2_score}")
            return game_over
        elif lines[0][14] == lines[2][14] == lines[4][14] == player_2:
            print("\nGame Over!\nPlayer 2 Wins!")
            self.player_2_score += 1
            print(f"Player 1 score: {self.player_1_score}\nPlayer 2 "
                  f"score: {self.player_2_score}")
            return game_over

    def draw_condition(self, game):
        game_over = True
        if '1' in game or '2' in game or '3' in game or '4' in game or '5' in game \
                or '6' in game or '7' in game or '8' in game or '9' in game:
            pass
        else:
            print("\nGame Over!\nThat's a Draw!")
            self.player_1_score += 0
            self.player_2_score += 0
            print(f"Player 1 score: {self.player_1_score}\nPlayer 2 "
                  f"score: {self.player_2_score}")
            return game_over
        return

    def tic_tac_toe(self, player1, player2, game_b):
        print(f"\n{game_b}")
        numbers = [num for num in range(1, 10)]
        choice_list = [str(num) for num in numbers]
        on = True
        while on:
            right_choice_1 = False
            while not right_choice_1:
                choice_1 = input("\nPlayer 1, your move (1-9): ")
                if choice_1 not in choice_list:
                    print("That's an invalid input. Type any number "
                          "between 1 and 9, both inclusive.")
                else:
                    right_choice_1 = True
                    game_b = game_b.replace(choice_1, player1)
            print(f"\n{game_b}")
            if self.win_condition(player_1=player1, player_2=player2, game=game_b):
                on = False
            elif self.draw_condition(game=game_b):
                on = False
            else:
                right_choice_2 = False
                while not right_choice_2:
                    choice_2 = input("\nPlayer 2, your move (1-9): ")
                    if choice_2 not in choice_list:
                        print("That's an invalid input. Type any number "
                              "between 1 and 9, both inclusive.")
                    else:
                        right_choice_2 = True
                        game_b = game_b.replace(choice_2, player2)
                print(f"\n{game_b}")
                if self.win_condition(player_1=player1, player_2=player2, game=game_b):
                    on = False
                elif self.draw_condition(game=game_b):
                    on = False
