#Daniel Alvarez
# #3/28/2019
#Programming Assignment 3

import Boggle



def main():

        points = 0
        print("Welcome to Boggle!")
        Bog = Boggle.Boggle(5)
        n = input("Enter a word: ")

        while True:
                if n != "quit":
                        Bog.check_word(n)

                        if Bog.check_word(n) == True:
                                print("word found")
                                points += 1
                                print("points:",points)
                        else:
                                print("word not found")

                        
                        n = input("Enter a word: ")
                else:
                        break
       
        print("Thank you for playing.\nYour score was:",points)


main()