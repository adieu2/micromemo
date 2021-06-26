from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Micromemo")
        self.pack(fill=BOTH, expand=1)

        self.card_frame = Frame(self, bg="#181818", highlightbackground="black", highlightthickness=1)
        self.card_frame.pack(fill=BOTH, expand=True, side=TOP)

        self.buttons_frame = Frame(self)
        self.buttons_frame.pack(fill=X, side=BOTTOM, padx=8, pady=8)

        self.question_label = Label(self.card_frame, text="Micromemo", borderwidth=2, relief="groove", fg="#00F")
        self.question_label.config(font=("Verdana", 36))
        self.question_label.pack(expand=True)

        self.answer_label = Label(self.card_frame, text="↙ Click « Load... »", borderwidth=2, relief="groove", fg="#0F0")
        self.answer_label.config(font=("Verdana", 36))
        self.answer_label.pack(expand=True)

        self.load_button = Button(self.buttons_frame, text="Load...", height=2)
        self.load_button.pack(side=LEFT)

        self.reverse_button = Button(self.buttons_frame, text="Flip", state=DISABLED, height=2)
        self.reverse_button.pack(side=LEFT)

        self.next_button = Button(self.buttons_frame, text="Start", state=DISABLED, height=2)
        self.next_button.pack(side=RIGHT)

    def client_exit(self):
        exit()
