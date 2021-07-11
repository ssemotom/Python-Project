#A Two Player Tic-Tac-Toe game in Python.

# The dictionary is used create the Tic-Tac-Toe board. The empty space field after every move,the value changes depending on the player's choice of move. 

ticTacToeBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
				'4': ' ' , '5': ' ' , '6': ' ' ,
				'1': ' ' , '2': ' ' , '3': ' ' }

boardKeys = []

for key in ticTacToeBoard:
    boardKeys.append(key)

# Function to print the updated board after every move in the game 

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# This is the main function which has all the game play functionalities.'''
def tGame():

    turn = 'P'
    count = 0


    for i in range(10):
        printBoard(ticTacToeBoard)
        print("Player," + turn + ", it is your turn to move.Please state the place where to Move:")

        move = input()        

        if ticTacToeBoard[move] == ' ':
            ticTacToeBoard[move] = turn
            count = count + 1
        else:
            print("The place is already filled.\nPlease state another place where to Move:")
            continue

        # After 5 moves, Check whether player P or Q has won.
        if count >= 5:
            if ticTacToeBoard['7'] == ticTacToeBoard['8'] == ticTacToeBoard['9'] != ' ': # across the top
                printBoard(ticTacToeBoard)
                print("\nThe game is over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif ticTacToeBoard['4'] == ticTacToeBoard['5'] == ticTacToeBoard['6'] != ' ': # across the middle
                printBoard(ticTacToeBoard)
                print("\nThe game is over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif ticTacToeBoard['1'] == ticTacToeBoard['2'] == ticTacToeBoard['3'] != ' ': # across the bottom
                printBoard(ticTacToeBoard)
                print("\nThe game is over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif ticTacToeBoard['1'] == ticTacToeBoard['4'] == ticTacToeBoard['7'] != ' ': # down the left side
                printBoard(ticTacToeBoard)
                print("\nThe game is over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif ticTacToeBoard['2'] == ticTacToeBoard['5'] == ticTacToeBoard['8'] != ' ': # down the middle
                printBoard(ticTacToeBoard)
                print("\nThe game is over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif ticTacToeBoard['3'] == ticTacToeBoard['6'] == ticTacToeBoard['9'] != ' ': # down the right side
                printBoard(ticTacToeBoard)
                print("\nThe game is over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif ticTacToeBoard['7'] == ticTacToeBoard['5'] == ticTacToeBoard['3'] != ' ': # diagonal
                printBoard(ticTacToeBoard)
                print("\nThe game is over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif ticTacToeBoard['1'] == ticTacToeBoard['5'] == ticTacToeBoard['9'] != ' ': # diagonal
                printBoard(ticTacToeBoard)
                print("\nThe game is over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        # In no player wins and the board is full, declare the result as 'tie'.
        if count == 9:
            print("\nThe Game Over.\n")                
            print("It's a Tie!!")

        # change the player after every move.
        if turn =='P':
            turn = 'Q'
        else:
            turn = 'P'        
    
    # Ask if a player wants to restart the game or not.
    restart = input("Do you want to play Again?(yes/no)")
    if restart == "yes" or restart == "Yes":  
        for key in boardKeys:
            ticTacToeBoard[key] = " "

        tGame()

if __name__ == "__main__":
    tGame()