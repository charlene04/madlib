import shutil
import os
import re
from tkinter import *
from tkinter import messagebox



SEPARATOR = "*"*80
SCREEN_WIDTH= shutil.get_terminal_size().columns
games_list = []



app = Tk()
v = IntVar()
app.title('Welcome to Sentence Generator GUI emulator')
# app.attributes('-fullscreen', True)
app.minsize(width=800, height=550)
app.maxsize(width=800, height=550)
app.columnconfigure(0, weight=1)
app.columnconfigure(1,  weight=1)

labelframe1 = LabelFrame(app, text="Choose a Template",  pady=20, padx=20)
labelframe1.grid(row=0, column=0, rowspan=2,  columnspan=2, sticky = NS)

labelframe2 = LabelFrame(app, text="Please fill in the Text Boxes", pady=10, padx=20)
labelframe2.grid(row=3, rowspan=9, column=0, columnspan=2, sticky = NS)

scrollbar = Scrollbar(labelframe2)
scrollbar.grid(row=3, column=2)

# labelframe2.configure(yscrollcommand=scrollbar.set)
# scrollbar.configure(command=labelframe2.yview)

def generate_sentence():
    print('OK')
    

    
def display_radio_buttons():
    Radiobutton(labelframe1, text='Be_Kind', variable=v, value=0 , anchor=W, command=generate_be_kind_template).pack(side=LEFT)
    Radiobutton(labelframe1, text='Letter_from_Camp', variable=v, value=1 , anchor=W, command=generate_letter_from_camp_template).pack(side=LEFT)
    Radiobutton(labelframe1, text='Romeo_and_Juliet', variable=v, value=2 , anchor=W, command=romeo_and_juliet).pack(side=LEFT)
    
def generate_be_kind_template():
    for widget in labelframe2.winfo_children():
        widget.destroy()
    games_list[0].display_input_fields()
    
def generate_letter_from_camp_template():
    for widget in labelframe2.winfo_children():
        widget.destroy()
    games_list[1].display_input_fields()
    
def romeo_and_juliet():
    for widget in labelframe2.winfo_children():
        widget.destroy()
    games_list[2].display_input_fields()


class AdLib(object):
    def __init__(self, title, template_string, required_inputs):
        self.title = title
        self.template_string = template_string
        self.input_type_list = required_inputs 
        self.variables = {}
        self.entry_boxes = {}
        self.input = []
        


   
       
    def display_input_fields(self):
        for index, input_type in enumerate(self.input_type_list):
            self.variables[f"input_text{index}"] = StringVar()
            input_label = Label(labelframe2, text=f"Enter a {input_type}: ",  font=('courier', 11), pady=5, padx=20)
            input_label.grid(row=int(f"{index}") + 2, column=0, sticky=W)
            self.entry_boxes[f"input_box{index}"] = Entry(labelframe2, textvariable=self.variables[f"input_text{index}"], justify=CENTER, font=('courier', 11), border=.5)
            self.entry_boxes[f"input_box{index}"].grid(row=int(f"{index}") + 2, column=1, sticky=W)
        gen_button = Button(labelframe2, text="Generate Sentence", width=18, command=self.generate_sentence, padx=8, pady=8)
        gen_button.grid(row=len(self.input_type_list) + 2, column=1, sticky = EW)
        
        gen_button = Button(labelframe2, text="Clear Input", width=18, command=self.clear_input, padx=8, pady=8)
        gen_button.grid(row=len(self.input_type_list) + 2, column=0, sticky=W)
        
    def clear_input(self):
        for entry in self.entry_boxes:
            self.entry_boxes[entry].delete(0, END)
        
        
    
    def generate_sentence(self):
        for variable_name in self.variables:
            if self.variables[variable_name].get() == '':
                messagebox.showerror('Required Fields', 'Please include all fields')
                return
            else:
                self.input.append(str(self.variables[variable_name].get()))
        
        for index in range(0, len(self.input)):
            string_index = str(index+1)
            string_index_bracketed = "["+string_index+"]"
            self.output_string = self.template_string.replace(string_index_bracketed, self.input[index] )
            self.template_string = self.output_string
        self.__print_output()

    def __print_output(self):
        app.clipboard_clear()
        app.clipboard_append(self.template_string)
        app.update() # now it stays on the clipboard after the window is closed
        messagebox.showinfo('Sentence Generated', self.template_string)
        self.clear_input()
            
    def __str__(self):
        return self.title

def prepare_game_data():
    # Three games are hardcoded
    be_kind = "Be kind to your [1]-footed [2]. For a duck may be somebody's [3]. Be kind to your [2] in [4]. Where the weather is always [5]. You may think that this is the [6]. Well it is."

    letter_from_camp = "Dear [1], I am having a(n) [2] time at camp. The counselour is [3] and the food is [4]. I met [5] and we became [6] friends. Unfortunately, [5] is [7] and I [8] my [9] so we couldn't go [10] like everybody else. I need more [11] and a [12] sharpener, so please [13] [14] more when you [15] back. Your [16], [17]" 

    romeo_and_juliet = "Two [1], both alike in dignity. In fair [2], where we lay our scene. From ancient [3] break to new mutiny,  where civil blood makes civil hands unclean. From forth the fatal loins of these two foes. A pair of star-cross'd [4] take their life; Whole misadventured piteous overthrows, do with their [5] bury their parents' strife. The fearful passage of their [6] love, And the continuance of their parents' rage, Which, but their children's end, nought could [7]. Is now the [8] hours' traffic of our stage; The which if you with [9] [10] attend, What here shall [11], our toil shall strive to mend."

    game1= AdLib("Be Kind", be_kind, ["NOUN", "NOUN(PLURAL)", "NOUN", "PLACE", "ADJECTIVE", "NOUN"])
    game2= AdLib("Letter From Camp", letter_from_camp, ["RELATIVE", "ADJECTIVE", "ADJECTIVE", "ADJECTIVE", "NAME OF PERSON IN ROOM", "ADJECTIVE", "ADJECTIVE", "VERB ENDING IN 'ED'", "BODY PART", "VERB ENDING IN 'ING'", "NOUN (PLURAL)","NOUN", "ADVERB", "VERB", "VERB", "RELATIVE", "PERSON IN ROOM"])
    game3 = AdLib("Romeo and Juliet", romeo_and_juliet, ["NOUN (PLURAL)", "PLACE", "NOUN", "NOUN (PLURAL)", "NOUN", "ADJECTIVE", "VERB", "NUMBER", "ADJECTIVE", "BODY PART", "VERB"])

    games_list.append(game1)
    games_list.append(game2)
    games_list.append(game3)


def start_game():
    display_radio_buttons()
    prepare_game_data()
    generate_be_kind_template()
   

if __name__ == "__main__":
    os.system('clear')
    start_game()
    

app.mainloop()

