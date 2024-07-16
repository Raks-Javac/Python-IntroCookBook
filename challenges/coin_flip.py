# ##### Challenge 7


#  7.⁠ ⁠Coin Flip Simulator:
# Create a program that simulates flipping a coin. Ask the user how many times they want to flip the coin, and then report the results (e.g., "Heads: 5, Tails: 3").


# ##### Challenge 9

#  9.⁠ ⁠Quiz Program:
# Create a program that asks users a series of questions, keeps track of their scores, and then reports their final score.


import random as rand

class CoinFlip:
    
    def __init__(self):
        self.total_flips = None
        self.choice_list = ['H','T']
        self.number_of_head = 0
        self.number_of_tail = 0
        self.total_h_t_list = []
    
    def welcome_user(self):
        print("Welcome to the coin flip app")
    def show_loading(self):
        print("Please wait while we process flip result")
    # take flip count from the user 
    def take_flip_count(self):
        try:
             flip_count = int(input("How many times should the coin be flipped? "))
             if flip_count != 0 or flip_count !=  "":
                 self.total_flips = flip_count
             else:
                 print("Flip count cannot be 0")
                 self.take_flip_count()
        except:
            print('Error taking flip count')
            self.take_flip_count()

    # start flipping using flip count 
    def start_flip(self):
        for _ in range(self.total_flips):
            choice_per_index = rand.choice(self.choice_list)
            print(choice_per_index)
            self.total_h_t_list.append(choice_per_index)
        for flip_rand in self.total_h_t_list:
            if(flip_rand == "H"):
                self.number_of_head+=1
            else:
                self.number_of_tail+=1
        print(f"Heads: {self.number_of_head}, Tails: {self.number_of_tail}")

    def start_app(self):
        self.welcome_user()
        self.take_flip_count()
        if self.total_flips != "" or self.total_flips is not None:
            self.show_loading()
            self.start_flip()       







coin_flip_app = CoinFlip()

# coin_flip_app.start_app()







