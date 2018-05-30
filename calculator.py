'''
A GUI calculator project written for #100daysofcode challenge
by Carlos del Rio
Twitter, Snapchat, & Instagram: @denverpedicab

Credit to http://khaliat.com/project-build-a-python-gui-calculator/ for
the great tutorial!
'''



from tkinter import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Tkinter Calculator")

        # Create a screen for the display
        self.screen = Text(master, state='disabled', width=30, height=3,
                            background="yellow", foreground="blue")

        # Set screen in window
        self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        self.screen.configure(state='normal')

        # Create variable for text inside screen
        self.screen_text =  ''

        # Create all buttons needed and store them in a dictionary
        buttons = {
            'b1': self.createButton(7),
            'b2': self.createButton(8),
            'b3': self.createButton(9),
            'b4': self.createButton(u"\u232B",None),
            'b5': self.createButton(4),
            'b6': self.createButton(5),
            'b7': self.createButton(6),
            'b8': self.createButton(u"\u00F7"),
            'b9': self.createButton(1),
            'b10': self.createButton(2),
            'b11': self.createButton(3),
            'b12': self.createButton('*'),
            'b13': self.createButton('.'),
            'b14': self.createButton(0),
            'b15': self.createButton('+'),
            'b16': self.createButton('-'),
            'b17': self.createButton('=',None,34)
            }

        # Create counters for rows and columns
        column_count = 0
        row_count = 1
        # Make a defualt span length and change it for the last button
        button_span = 1
        # Arrange buttons with grid manager
        for button in buttons:
            if column_count == 4:
                row_count += 1
                column_count = 0
            # Check if last button, if so, change span length
            if button == 'b17':
                button_span = 4
            buttons[button].grid(row=row_count, column=column_count,
                                columnspan=button_span)
            column_count += 1

    # Function to create buttons on demand with a lable equal to the value
    def createButton(self, val, write=True, width=7):
        return Button(self.master, text=val,
                        command = lambda: self.click(val,write), width=width)

    def click(self,text,write):
        # This function handles clicking of the buttons
        if write == None and text == '=' and self.screen_text:
            #replace division symbol with slash for evaluation
            self.screen_text = re.sub(u"\00F7",'/',self.screen_text)
            print(self.screen_text)
            answer = str(eval(self.screen_text))
            self.clear_screen()
            self.insert_screen(answer,newline=True)
        elif write == None and text == u"\u232B":
            # If text is backline character clear the screen
            self.clear_screen()
        else:
            # Else insert text into screen
            self.insert_screen(text)

    def clear_screen(self):
        # Clear screen by setting screen_text to empty
        self.screen_text = ''
        self.screen.configure(state='normal')
        self.screen.delete('1.0', END)

    def insert_screen(self, value, newline=False):
        self.screen.configure(state='normal')
        self.screen.insert(END, value)
        self.screen_text += str(value)
        self.screen.configure(state='disabled')

# Create window object
root = Tk()
# Pass object into Calculator class
calc_gui = Calculator(root)
# Run mainloop to capture events in window.
root.mainloop()
