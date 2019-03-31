#Daniel Alvarez
#3/28/2019
#Programming Assignment 3

import Boggle


def main():
        
        print("Welcome to Boggle!")
        print("To quit the game, type 'quit' in all lower case letters")
        Bog = Boggle.Boggle(5)
        n = str(input("Enter a word: "))
        Bog.check_word(n)

main()