import numpy as np
import time as t
import window as w

class Game:
    def __init__(self, buttonlist):
        self.turn = 0
        self.grid = [0] * 9
        self.buttonlist = buttonlist


    def reset_Button(self):
        for button in self.buttonlist:
            button["text"] = " "
    
    #start new game
    def new_Game(self):
        self.grid = [0] * 9
        self.turn = 0
        self.reset_Button()

    #check if someone won
    def check(self):
        #reshape grid to 3x3 matrix
        matrix = np.array(self.grid).reshape(3, 3)

        #row and column
        for i in range(matrix.shape[0]):
            #row
            if np.all(matrix[i,:] == matrix[i, 0]) and matrix[i, 0]:
                print(f"\nGame Over! {'X' if matrix[i, 0] == 1 else 'O'} wins")
                self.new_Game()
            #column
            elif np.all(matrix[:, i] == matrix[0, i]) and matrix[0, i]:
                print(f"\nGame Over! {'X' if matrix[0, i] == 1 else 'O'} wins")
                self.new_Game()
        
        # Check if all values in the main diagonal are the same
        if np.all(np.diagonal(matrix) == matrix[0, 0]) and matrix[0, 0] != 0:
            print(f"\nGame Over! {'X' if matrix[0, 0] == 1 else 'O'} wins")
            self.new_Game()

        # Check if all values in the anti-diagonal are the same
        elif np.all(np.diagonal(np.fliplr(matrix)) == matrix[0, -1]) and matrix[0, -1] != 0:
            print(f"\nGame Over! {'X' if matrix[0, -1] == 1 else 'O'} wins")
            self.new_Game()
    
    #mark a spot x or o
    def mark(self, buttonlist, pos):

        if buttonlist[pos]["text"] != " ":
            pass
        elif self.turn % 2 == 0:
            buttonlist[pos]["text"] = "X"
            self.grid[pos] = 1
            self.turn += 1
        else:
            buttonlist[pos]["text"] = "O"
            self.grid[pos] = 2
            self.turn += 1
        self.check()