# ##### Challenge 5

#  5.⁠ ⁠Mad Libs:
# Create a program that asks users for words (e.g., noun, verb, adjective) and then uses them to generate a funny story.





class Mab_Lib:
    def __init__(self):
        self.noun = None
        self.verb = None
        self.adjective = None
        self.story = None

    def get_word(self,word_type):
        return input(f"Please enter a {word_type}: ")
    def create_story(self):
        return f"Once upon a time, there was a {self.adjective} {self.noun} who loved to {self.verb} all day long. One day, the {self.noun} decided to {self.verb} to the moon. It was the most {self.adjective} adventure ever!"
    def mat_lib_app(self):
        self.noun = self.get_word("noun")
        self.verb = self.get_word("verb")
        self.adjective = self.get_word("adjective")
        
        self.story = self.create_story()
        
        print("\nHere is your funny story:")
        print(self.story)



mat_lib_app = Mab_Lib()




