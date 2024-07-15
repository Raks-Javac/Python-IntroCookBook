# ##### Challenge 3

#  3.⁠ ⁠Rock, Paper, Scissors:
# Create a program that allows two players to play Rock, Paper, Scissors. Ask each player for their choice (rock, paper, or scissors), and then determine the winner.





class RockPaperSis: 
    def __init__(self):
        self.game_list = ['r','p','s']
        self.winner = None
        self.player1 = None
        self.player2 = None
    
    def run_welcome(self):
        print("Welcome to 🪨 and ✌️ Game \nr for (rock)🪨 \np for paper \ns for (scisccors)✌️ ")
        # player 1 sessiom
    def player_1(self):
        try:
            p1 = str(input("Player 1: ")).lower()
            if p1 in self.game_list:
                self.player1 = p1           
            else:
                print("Option not in game")
                self.player_1()
        except:
            print("Error occured processing, kindly check input")
            self.player_1()

            # player 2 session
    def player_2(self):
        try:
            p2 = str(input("Player 2: ")).lower()
            if p2 in self.game_list:
                self.player2 = p2
            else:
                print("Option not in game")
                self.player_2()                
        except:
            print("Error occured processing, kindly check input")
            self.player_2()

#  using both players input check the winner with the rock paper sis logic 
# Rock beats Scissors: Rock crushes Scissors.
# Scissors beat Paper: Scissors cut Paper.
# Paper beats Rock: Paper covers Rock.

    def win_codition(self):
        if self.player1 == "r" and self.player2 == "p":
            print("Player 2 win, paper wins over rock")
        elif self.player1 == "p" and self.player2 == "s": 
            print("Player 2 win, scisscors wins over paper")
        elif self.player1 == "s" and self.player2 == "r": 
            print("Player 2 win, rock wins over scissors")
        elif self.player2 == "r" and self.player1 == "p":
            print("Player 1 win, paper wins over rock")
        elif self.player2 == "p" and self.player1 == "s": 
            print("Player 1 win, scisscors wins over paper")
        elif self.player2 == "s" and self.player1 == "r": 
            print("Player 1 win, rock wins over scissors")       
        
        
        # This method is called to start game 
    def start_game(self):
        self.run_welcome()
        self.player_1()
        if self.player1 is not None: 
            self.player_2()
            if self.player2 is not None:
                self.win_codition()
    
 

#  initialize object

rock_app = RockPaperSis()
