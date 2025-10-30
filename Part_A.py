"""
Tic-Tac-Toe

This program is a simple Tic-Tac-Toe game using classes and objects.
    
    
"""

class Board: 
    def __init__(self): 
        #3x3 2d list of strings 

        #print new board 
        self.c = [[" "," "," "],
                  [" "," "," "],
                  [" "," "," "]]
        
    def printBoard(self):
        # it first prints the BOARD_HEADER constant
        # BOARD_HEADER constant
        BOARD_HEADER = "-----------------\n|R\\C| 0 | 1 | 2 |\n-----------------"
        print(BOARD_HEADER)

        # using a for-loop, it increments through the rows
        for i in range(3):
            print(f"| {i} | {self.c[i][0]} | {self.c[i][1]} | {self.c[i][2]} |")
            print("-----------------")

class Game: 
    def __init__(self): 
        #initalizes game board and starts with player X 
        self.board = Board() 
        self.turn = 'X'

    def switchPlayer(self): 
        if self.turn == "X":
            self.turn ="O"
        else: 
            self.turn = "X"
    
    def validateEntry(self, row, col): 
        print(f"You have entered row #{row}\n\t  and1 column #{col}")

        if row not in (0, 1, 2) or col not in (0, 1, 2):
            print("Invalid entry: try again.\nRow & column numbers must be either 0, 1, or 2.")
            return False
        if self.board.c[row][col] != " ":
            print("That cell is already taken. \nPlease make another selection.")
            return False
        else: 
            print("Thank you for your selection.") 
            return True 
        
    def checkFull(self): 
    # returns True if the board is full, otherwise False
        for row in self.board.c:
            for col in row:  
                if col == " ":  # found an empty space
                    return False
        
        print("DRAW! NOBODY WINS!")
        return True
    
    def checkWin(self): 
        #rows
        b = self.board.c 
        t = self.turn 

        for r in range(3):
            if b[r][0] == b[r][1] == b[r][2] == t:
                print(f"{t} IS THE WINNER!!!")
                return True

        # check columns
        for c in range(3):
            if b[0][c] == b[1][c] == b[2][c] == t:
                print(f"{t} IS THE WINNER!!!")
                return True

        # check diagonals
        if (b[0][0] == b[1][1] == b[2][2] == t) or (b[0][2] == b[1][1] == b[2][0] == t):
            print(f"{t} IS THE WINNER!!!")
            return True

        return False
    
    def checkEnd(self): 
        #returns True if game is over, otherwise False
        if self.checkWin() or self.checkFull():
            return True
        else: 
            return False
    
    def playGame(self): 
        self.board = Board()
        self.turn = "X"
        print(f"New game:{self.turn} goes first.\n")      

        while True: 
            self.board.printBoard() 
            print(f"\n{self.turn}'s turn.")
            print(f"Where do you want your {self.turn} placed? ")
            entry = input("Please enter row number and column number separated by a comma.\n").split(",")
            row = int(entry[0])
            col = int(entry[1])

            isValid = self.validateEntry(row, col)
            if not isValid:
                continue
            #run validEntry again if validate Entry is false 
        
        
            self.board.c[row][col] = self.turn

            if self.checkEnd():
                self.board.printBoard()
                break

            self.switchPlayer()



def main():
    again = "y"

    while again.lower() == "y": 
            game = Game() 
            game.playGame()
            again = input("\nAnother game? Enter Y or y for yes.\n")
            
            
    print("Thank you for playing!")
 

#calls main function 
if __name__ == "__main__": 
    main() 