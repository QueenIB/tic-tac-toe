print("\nThis is a Text-based Version of the Famous Tic Tac Toe Game, "
      "Otherwise Known as Xs and Os.\n")
print("Rule of the game: the numbers in the game board below represent the spaces"
      "where your Xs and Os will go in.\nType the number in the space you want to"
      " place your X or O, and the number will be replaced with your X or O.")

game_board = ("  1  |  2  |  3  \n-----------------\n  4  |  5  |  6  \n------------"
              "-----\n  7  |  8  |  9  ")

players = ['X', 'O']
choice = input(f"\nPlayer 1 select X or O: ").lower()
if choice == 'x':
    player1 = players[0]
    player2 = players[1]
else:
    player1 = players[1]
    player2 = players[0]


def tic_tac_toe(game_b):
    print(f"\n{game_b}")
    on = True
    while on:
        choice_1 = input("\nPlayer 1, your move (1-9): ")
        game_b = game_b.replace(choice_1, player1)
        print(f"\n{game_b}")
        if win_condition(player_1=player1, player_2=player2, game=game_b):
            on = False
        else:
            choice_2 = input("\nPlayer 2, your move (1-9): ")
            game_b = game_b.replace(choice_2, player2)
            print(f"\n{game_b}")
            if win_condition(player_1=player1, player_2=player2, game=game_b):
                on = False


def win_condition(player_1, player_2, game):
    lines = game.split('\n')
    game_over = True
    if lines[0][2] == lines[0][8] == lines[0][14] == player_1:
        print("\nGame Over!\nPlayer 1 Wins!")
        return game_over
    elif lines[0][2] == lines[0][8] == lines[0][14] == player_2:
        print("\nGame Over!\nPlayer 2 Wins!")
        return game_over
    elif lines[2][2] == lines[2][8] == lines[2][14] == player_1:
        print("\nGame Over!\nPlayer 1 Wins!")
        return game_over
    elif lines[2][2] == lines[2][8] == lines[2][14] == player_2:
        print("\nGame Over!\nPlayer 2 Wins!")
        return game_over
    elif lines[4][2] == lines[4][8] == lines[4][14] == player_1:
        print("\nGame Over!\nPlayer 1 Wins!")
        return game_over
    elif lines[4][2] == lines[4][8] == lines[4][14] == player_2:
        print("\nGame Over!\nPlayer 2 Wins!")
        return game_over
    elif lines[0][2] == lines[2][8] == lines[4][14] == player_1:
        print("\nGame Over!\nPlayer 1 Wins!")
        return game_over
    elif lines[0][2] == lines[2][8] == lines[4][14] == player_2:
        print("\nGame Over!\nPlayer 2 Wins!")
        return game_over
    elif lines[0][14] == lines[2][8] == lines[4][2] == player_1:
        print("\nGame Over!\nPlayer 1 Wins!")
        return game_over
    elif lines[0][14] == lines[2][8] == lines[4][2] == player_2:
        print("\nGame Over!\nPlayer 2 Wins!")
        return game_over
    elif lines[0][2] == lines[2][2] == lines[4][4] == player_1:
        print("\nGame Over!\nPlayer 1 Wins!")
        return game_over
    elif lines[0][2] == lines[2][2] == lines[4][4] == player_2:
        print("\nGame Over!\nPlayer 2 Wins!")
        return game_over
    elif lines[0][8] == lines[2][8] == lines[4][8] == player_1:
        print("\nGame Over!\nPlayer 1 Wins!")
        return game_over
    elif lines[0][8] == lines[2][8] == lines[4][8] == player_2:
        print("\nGame Over!\nPlayer 2 Wins!")
        return game_over
    elif lines[0][14] == lines[2][14] == lines[4][14] == player_1:
        print("\nGame Over!\nPlayer 1 Wins!")
        return game_over
    elif lines[0][14] == lines[2][14] == lines[4][14] == player_2:
        print("\nGame Over!\nPlayer 2 Wins!")
        return game_over


game_on = True
while game_on:
    tic_tac_toe(game_b=game_board)
    want_to_continue = input("\nDo you want to play again? "
                             "type 'yes' or 'no': ").lower()
    if want_to_continue == 'no':
        game_on = False
