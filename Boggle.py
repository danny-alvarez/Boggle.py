import random
import copy
#import Cell
#The Boggle Class
class Boggle:
    def __init__(self, n):
        """Initializes the Boggle class and the board"""
        self.board = []
        self.n = n

        #Return an error if it's not a string
        if type(n) != int or n < 1:
            """Checks if it is a positive integer"""
            return ValueError('n must be a positive integer')
       
        #create first board
        for row in range(n):
            """Adds row to board"""
            self.board.append([])
            for col in range(n):
                """Generates random letters from A-Z in board"""
                self.ranInt= random.randint(ord('A'), ord('Z'))

                """Places letters into board"""
                self.board[row].append(chr(self.ranInt))
                print(chr(self.ranInt),end=" ")
            print("")        
    
          
    
    def check_word(self, string):
     
        '''takes in a word and returns a boolean if
        the word is in the list then return true'''

        word = string.split()
        startingPoint = word[0]
        
        #Get into the board
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                #Find first letter as a starting point
                if self.board[row][col] == startingPoint:
                    print("found ",startingPoint, "at ",row,col)


          
