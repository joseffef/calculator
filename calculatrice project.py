from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("357x420+0+0")
        master.config(bg="black")
        master.resizable(False, False)

        self.is_dark_mode = True
        self.equation = StringVar()
        self.entry_value = ""
        self.buttons = []

        # Entry field at the top
        self.entry = Entry(width=17, bg="black", fg="white", 
                          font=('Arial Bold', 32), 
                          textvariable=self.equation, 
                          insertbackground="white")
        self.entry.place(x=0, y=0)

        # Button configurations
        button_font = ('Arial Bold', 16)
        button_width = 11
        button_height = 4
        
        # Button layout data: (text, fg_color, x, y, command)
        buttons_data = [
            # Row 1
            ('C', 'blue', 0, 50, self.clear),
            ('(', 'blue', 90, 50, lambda: self.show('(')),
            (')', 'blue', 180, 50, lambda: self.show(')')),
            ('/', 'blue', 270, 50, lambda: self.show('/')),
            
            # Row 2
            ('7', 'white', 0, 125, lambda: self.show(7)),
            ('8', 'white', 90, 125, lambda: self.show(8)),
            ('9', 'white', 180, 125, lambda: self.show(9)),
            ('x', 'blue', 270, 125, lambda: self.show('*')),
            
            # Row 3
            ('4', 'white', 0, 200, lambda: self.show(4)),
            ('5', 'white', 90, 200, lambda: self.show(5)),
            ('6', 'white', 180, 200, lambda: self.show(6)),
            ('-', 'blue', 270, 200, lambda: self.show('-')),
            
            # Row 4
            ('1', 'white', 0, 275, lambda: self.show(1)),
            ('2', 'white', 90, 275, lambda: self.show(2)),
            ('3', 'white', 180, 275, lambda: self.show(3)),
            ('+', 'blue', 270, 275, lambda: self.show('+')),
            
            # Row 5
            ('%', 'white', 0, 350, lambda: self.show('%')),
            ('0', 'white', 90, 350, lambda: self.show(0)),
            ('.', 'white', 180, 350, lambda: self.show('.')),
            ('=', 'white', 270, 350, lambda: self.evaluate()),
        ]

        # Create buttons
        for (text, fg_color, x, y, cmd) in buttons_data:
            # Special case for equals button
            bg_color = 'blue' if text == '=' else '#333333'
            
            btn = Button(
                width=button_width,
                height=button_height,
                text=text,
                relief='flat',
                fg=fg_color,
                bg=bg_color,
                font=button_font,
                command=cmd
            )
            btn.place(x=x, y=y)
            self.buttons.append(btn)

        # Add theme toggle button
        theme_btn = Button(
            width=5,
            height=1,
            text='Theme',
            relief='flat',
            fg='white',
            bg='#333333',
            font=('Arial Bold', 10),
            command=self.toggle_theme
        )
        theme_btn.place(x=300, y=10)
        self.buttons.append(theme_btn)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def evaluate(self):
        result = eval(self.entry_value)
        self.equation.set(result)
    
    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        
        # Set colors based on mode
        bg_color = "black" if self.is_dark_mode else "white"
        fg_color = "white" if self.is_dark_mode else "black"
        button_bg = "darkgray" if self.is_dark_mode else "lightgray"
        
        # Update window background
        self.master.config(bg=bg_color)
        
        # Update entry colors including insertion cursor
        self.entry.config(bg=bg_color, fg=fg_color, insertbackground=fg_color)
        
        # Update all button colors
        for button in self.buttons:
            button.config(bg=button_bg, fg=fg_color)

root = Tk()
calc = Calculator(root)
root.mainloop()