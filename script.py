from connect_four import *

def two_ai_game():
    my_board = make_board()
    while not game_is_over(my_board):
      #The "X" player finds their best move.
      result = minimax(my_board, True, 4, -float("Inf"), float("Inf"), my_evaluate_board)
      print( "X Turn\nX selected ", result[1])
      print(result[1])
      select_space(my_board, result[1], "X")
      print_board(my_board)

      if not game_is_over(my_board):
        #The "O" player finds their best move
        result = minimax(my_board, False, 3, -float("Inf"), float("Inf"), codecademy_evaluate_board)
        print( "O Turn\nO selected ", result[1])
        print(result[1])
        select_space(my_board, result[1], "O")
        print_board(my_board)
    if has_won(my_board, "X"):
        print("X won!")
    elif has_won(my_board, "O"):
        print("O won!")
    else:
        print("It's a tie!")

#two_ai_game()


# Testing our evaluation func
new_board = make_board()
select_space(new_board, 1, "X")
select_space(new_board, 1, "X")
select_space(new_board, 2, "X")
select_space(new_board, 2, "X")
select_space(new_board, 3, "O")
select_space(new_board, 3, "O")
select_space(new_board, 4, "O")
select_space(new_board, 4, "O")

print_board(new_board)
print(my_evaluate_board(new_board))