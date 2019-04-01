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
    
        self.userBoard = copy.deepcopy(self.board)

    def displayBoard(self):
        for row in self.userBoard:
            for col in row:
                print(col, "", end="")
            print("")
    
    def check_word(self, word):
     
        '''takes in a word and returns a boolean if
        the word is in the list then return true'''

        
        firstLetter = word[0]
        lastLetter = word[0]

        if len(word) == 1:
            return True
        else:
            #only see shit if the firstletter is in the board
            for row in range(len(self.board)):
                if firstLetter in self.board[row]:
                    #search to the right and left
                    if word[1:] in self.board[row]:
                        return True
                    #Search up and down
                    elif word[1:] not in self.board[row]:
            
                    #Search downward
                        if word[1:] in self.board[row+1]:
                            return True

                        #Search upward
                        if word[1:] in self.board[row-1]:
                            return True
            
        
        self.displayBoard()
                
                    
