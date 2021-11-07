import shutil
import os
import re

SEPARATOR = "*"*80
SCREEN_WIDTH= shutil.get_terminal_size().columns
games_list = []

def print_center(input_string, end_char = "\n"):
    half_len = len(input_string) / 2
    half_width= SCREEN_WIDTH / 2
    start_pos = half_width - half_len 

    if "\033[9" in input_string:
        count = input_string.count("\033[9")
        string_len = len(input_string) + (count*4) 
    else:
        string_len = len(input_string)

    print(input_string.rjust(string_len + int(start_pos)), end = end_char)

class AdLib(object):
    def __init__(self, title, template_string, required_inputs):
        self.title = title
        self.template_string = template_string
        self.input_type_list = required_inputs 
        self.input = []

    def play_terminal_game(self): 
        print_center(SEPARATOR)
        print_center(self.title.upper())
        print_center(SEPARATOR)
        self.__get_input()

        for index in range(0, len(self.input)):
            string_index = str(index+1)
            string_index_bracketed = "["+string_index+"]"
            self.output_string = self.template_string.replace(string_index_bracketed, "\033[9{0}m".format((index%7)+1) + self.input[index] +"\033[00m")
            self.template_string = self.output_string
        
        self.__print_output()
    
    def __get_input(self): 
        for input_type in self.input_type_list:
            print_center(f"Enter a {input_type}: ", "")
            self.input.append(str(input()))
        
        print_center(SEPARATOR)
        print_center("Press ENTER to go mad!!!")
        print_center(SEPARATOR, "")
        input()

    def __print_output(self):
        print_center("Output:")
        print_center(SEPARATOR)
        print()
        print_center(self.title)
        print()
        print_center(SEPARATOR)

        for line in self.output_string.split("\n"):
            print_center(line)

def prepare_game_data():
    # Three games are hardcoded
    be_kind = "Be kind to your [1]-footed [2] \nFor a duck may be somebody's [3] \nBe kind to your [2] in [4]\nWhere the weather is always [5].\nYou may think that this is the [6],\nWell it is."

    letter_from_camp = "Dear [1],\nI am having a(n) [2] time at camp. The \ncounselour is [3] and the food is\n[4]. I met [5] and we\nbecame [6] friends. Unfortunately,\n[5] is [7] and I\n[8] my [9] so we couldn't\ngo [10] like everybody else. I need more\n[11] and a [12] sharpener,\nso please [13] [14] more\nwhen you [15] back.\nYour [16],\n[17]" 

    romeo_and_juliet = "Two [1], both alike in dignity,\nIn fair [2], where we lay our scene,\nFrom ancient [3] break to new mutiny,\nWhere civil blood makes civil hands unclean.\nFrom forth the fatal loins of these two foes\nA pair of star-cross'd [4] take their life;\nWhole misadventured piteous overthrows\nDo with their [5] bury their parents' strife.\nThe fearful passage of their [6] love,\nAnd the continuance of their parents' rage,\nWhich, but their children's end, nought could\n[7],\nIs now the [8] hours' traffic of our stage;\nThe which if you with [9]\n[10] attend,\nWhat here shall [11], our toil shall strive to\nmend."

    game1= AdLib("Be Kind", be_kind, ["NOUN", "NOUN(PLURAL)", "NOUN", "PLACE", "ADJECTIVE", "NOUN"])
    game2= AdLib("Letter From Camp", letter_from_camp, ["RELATIVE", "ADJECTIVE", "ADJECTIVE", "ADJECTIVE", "NAME OF PERSON IN ROOM", "ADJECTIVE", "ADJECTIVE", "VERB ENDING IN 'ED'", "BODY PART", "VERB ENDING IN 'ING'", "NOUN (PLURAL)","NOUN", "ADVERB", "VERB", "VERB", "RELATIVE", "PERSON IN ROOM"])
    game3 = AdLib("Romeo and Juliet", romeo_and_juliet, ["NOUN (PLURAL)", "PLACE", "NOUN", "NOUN (PLURAL)", "NOUN", "ADJECTIVE", "VERB", "NUMBER", "ADJECTIVE", "BODY PART", "VERB"])

    games_list.append(game1)
    games_list.append(game2)
    games_list.append(game3)

def start_game():
    print_center(SEPARATOR)
    print_center("MADLIBS GAME")
    print_center(SEPARATOR)
    print()
    print_center("Choose a game to play: 1/2/3")
    print()
    print_center(SEPARATOR)
    print()

    for game in games_list: 
        print_center(str(games_list.index(game)+1) + f": {game.title}")

    print_center("1/2/3: ", "")
    game_choice = input("")
    games_list[int(game_choice)-1].play_terminal_game()

if __name__ == "__main__":
    os.system('clear')
    prepare_game_data()
    start_game()
