from funcs import TicTacToe

print("\nThis is a Text-based Version of the Famous Tic Tac Toe Game, "
      "Otherwise Known as Xs and Os.\n")
print("How to play: the numbers in the game board below represent the spaces"
      "where your Xs and Os will go in.\nType the number in the space in which "
      "you want to place your X or O, and the number will be replaced with your "
      "X or O.")

game_board = ("  1  |  2  |  3  \n-----------------\n  4  |  5  |  6  \n------------"
              "-----\n  7  |  8  |  9  ")


players = ['X', 'O']
player1 = ''
player2 = ''
player_choice = False
while not player_choice:
    choice = input(f"\nPlayer 1 select X or O: ").lower()
    if choice != 'x' and choice != 'o':
        print("That's an invalid input. Type X or O.")
    elif choice == 'x':
        player1 = players[0]
        player2 = players[1]
        player_choice = True
    else:
        player1 = players[1]
        player2 = players[0]
        player_choice = True

game = TicTacToe()
game_on = True
while game_on:
    game.tic_tac_toe(game_b=game_board, player1=player1, player2=player2)
    prompt = True
    while prompt:
        want_to_continue = input("\nDo you want to play again? "
                                 "Type 'yes' or 'no': ").lower()
        if want_to_continue != 'yes' and want_to_continue != 'no':
            print("That's an invalid input. Type yes or no.")
        elif want_to_continue == 'no':
            print(f"Final Scores:\nPlayer 1: {game.player_1_score}\nPlayer 2: "
                  f"{game.player_2_score}")
            prompt = False
            game_on = False
        else:
            prompt = False
