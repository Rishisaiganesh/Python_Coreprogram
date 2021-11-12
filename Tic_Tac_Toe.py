
'''
@Auther:Rishisaiganesh
@Date: 12-11-2021
@Title:TO Play Cross game or TIC_TAC_TOE
'''
#Board
def print_tic_tac_toe(values):
    print("")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('_____|_____|_____')
 
    print("    |     |")
    print(" {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('_____|_____|_____')
 
    print("     |     |")
 
    print("  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("     |     |")
    print("")
 
#Scoreboard
def print_scoreboard(score_board):
   
    players = list(score_board.keys())
    print("  ", players[0], "   ", score_board[players[0]])
    print("   ", players[1], "   ", score_board[players[1]])
 
 
def check_win(player_pos, cur_player):
 
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    for x in soln:
        if all(y in player_pos[cur_player] for y in x):

            return True      
    return False       
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False       
 
def single_game(cur_player):
 
 
    values = [' ' for x in range(9)]

    player_pos = {'X':[], 'O':[]}
     
    while True:
        print_tic_tac_toe(values)
         
        try:
            print("Player ", cur_player, " Which box? : ", end="")
            move = int(input()) 
        except ValueError:
            print("Input was wrong")
            continue
 
        if move < 1 or move > 9:
            print("Input was wrong")
            continue
 
        if values[move-1] != ' ':
            print("this place is allready fill")
            continue
        values[move-1] = cur_player

        player_pos[cur_player].append(move)
 
        if check_win(player_pos, cur_player):
            print_tic_tac_toe(values)
            print("Player ", cur_player, "  won the game")     
            return cur_player
        if check_draw(player_pos):
            print_tic_tac_toe(values)
            print("Game Tie")
            return 'D'

        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'
 
if __name__ == "__main__":
 
    print("Player 1")
    player1 = input("Enter the name : ")
    print("\n")
 
    print("Player 2")
    player2 = input("Enter the name : ")
    print(" ")
     
    #player  chooses X and O
    cur_player = player1
 
    # Stores the choice of players
    player_choice = {'X' : "", 'O' : ""}
 
    options = ['X', 'O']

    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board)
 
    while True:
 
        print("Turn to choose for", cur_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")
 
        try:
            choice = int(input())   
        except ValueError:
            print("Wrong Input ")
            continue
  
        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1
 
        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1
         
        elif choice == 3:
            print("Final Scores")
            print_scoreboard(score_board)
            break  
 
        else:
            print("Wrong Choice1")
        winner = single_game(options[choice-1])
         
        if winner != 'D' :
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1
 
        print_scoreboard(score_board)
        if cur_player == player1:
            cur_player = player2
        else:
            cur_player = player1

