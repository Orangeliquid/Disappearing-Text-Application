import tkinter as tk
from tkinter import messagebox


def help_message():
    messagebox.showinfo(title="Help",
                        message="Welcome to Help!\n\nFirst: Click the text box, once clicked the timer will start\n"
                                "\nSecond: Start typing, maybe start with a sentence or a story!\n"
                                "\nThird: There is a timer that counts down and if it reaches 0 all text will delete.\n"
                                "\nSee how long you can continue to type!\n"
                        )


def about_message():
    messagebox.showinfo(title="About this app",
                        message="This is my take on a disappearing text app. I utilize the color Orange because I truly"
                                " love the color. I am a new software developer that enjoys learning by doing. "
                                "Feel free to use this app, whether as a personal app, or build your own"
                                " rendition with my app as a starting point! Enjoy!"
                        )


class PlaceholderText(tk.Text):
    def __init__(self, master=None, placeholder=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder

        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)

        self.add_placeholder()

    def on_focus_in(self, event):
        if self.get("1.0", "end-1c") == self.placeholder:
            self.delete("1.0", "end-1c")
            self.configure(fg="black")  # Set text color to black when focused

    def on_focus_out(self, event):
        if not self.get("1.0", "end-1c"):
            self.add_placeholder()
            self.configure(fg="grey")  # Set text color to grey when not focused

    def add_placeholder(self):
        self.insert("1.0", self.placeholder)
        self.configure(fg="grey")  # Set initial text color to grey


class DisappearingText:
    def __init__(self):
        # Timer and text tracking creation
        self.timer_count = 5
        self.timer = self.timer_count
        self.has_typed = False

        # TK window creation
        self.window = tk.Tk()
        self.window.title("Disappearing Text Application")
        self.window.config(bg="#FFDEAD")
        self.window.geometry("800x350")

        # Text box creation using PlaceholderText
        self.text = PlaceholderText(self.window, placeholder="Type here to start.", height=5, width=52, wrap="word", font=("Arial", 20), spacing1=8, spacing2=12, spacing3=12)
        self.text.grid(row=1, column=2, columnspan=3, rowspan=5, pady=20, padx=10)

        # Help button and grid
        self.help_button = tk.Button(text="Help", width=8, bg="#ADCEFF", font="Futura", command=help_message)
        self.help_button.grid(row=6, column=2, padx=10, sticky="w")

        # About button creation and grid
        self.about_button = tk.Button(width=8, text="About", bg="#ADCEFF", font="Futura", command=about_message)
        self.about_button.grid(row=6, column=4, padx=10, sticky="e")

        # Timer creation
        self.time_count_label = tk.Label(text=self.timer, width=8, bg="#ADCEFF", font="Futura", relief=tk.SOLID)
        self.time_count_label.grid(row=6, column=3, pady=10)

        self.text.bind("<Key>", self.started_typing)
        tk.mainloop()

    def reset_timer(self):
        self.timer = self.timer_count

    def reset_app(self):
        self.text.delete(1.0, "end")
        self.has_typed = False
        self.reset_timer()

    def countdown(self):
        if self.has_typed:
            self.timer -= 1
            if self.timer == 0:
                self.reset_app()
            self.time_count_label.config(text=self.timer)
            self.window.after(1000, self.countdown)

    def started_typing(self, event):
        if self.has_typed:
            self.reset_timer()
        else:
            self.has_typed = True
            self.countdown()


if __name__ == "__main__":
    DisappearingText()
