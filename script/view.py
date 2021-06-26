from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Micromemo")
        self.pack(fill=BOTH, expand=1)

        self.card_frame = Frame(self, bg="#888", highlightbackground="black", highlightthickness=1)
        self.card_frame.pack(fill=BOTH, expand=True, side=TOP)

        self.buttons_frame = Frame(self)
        self.buttons_frame.pack(fill=X, side=BOTTOM, padx=8, pady=8)

        self.question_label = Label(self.card_frame, text="Micromemo", borderwidth=2, relief="groove")
        self.question_label.config(fg="#00F", bg="#999")
        self.question_label.config(font=("Verdana", 36))
        self.question_label.pack(expand=True)

        self.answer_label = Label(self.card_frame, text="↙ Click « Load... »", borderwidth=2, relief="groove")
        self.answer_label.config(fg="#0F0", bg="#999")
        self.answer_label.config(font=("Verdana", 36))
        self.answer_label.pack(expand=True)

        self.load_button = Button(self.buttons_frame, text="Load...", height=2)
        self.load_button.pack(side=LEFT)

        self.reverse_button = Button(self.buttons_frame, text="Flip", state=DISABLED, height=2)
        self.reverse_button.pack(side=LEFT)

        self.next_button = Button(self.buttons_frame, text="Start", state=DISABLED, height=2)
        self.next_button.pack(side=RIGHT)

    def get_ready(self, message):
        self.reverse_button.config(state=NORMAL)
        self.next_button.config(text="Start", state=NORMAL)
        self.question_label.config(text=message)
        self.answer_label.config(text="Click « Start » ↘")
        self.answer_label.pack(expand=True)

    def prompt_question(self, question, answer):
        self.question_label.config(text=question)
        self.answer_label.config(text=answer)
        self.answer_label.pack_forget()
        self.next_button.config(text="Show answer")

    def show_answer(self):
        self.answer_label.pack(expand=True)
        self.next_button.config(text="Next card")

    def client_exit(self):
        exit()
