from tkinter import filedialog
from tkinter import *

class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.configure_events(view)

    def configure_events(self, view):
        view.load_button.config(command=self.load_deck)
        view.next_button.config(command=self.next_or_flip_card)
        view.reverse_button.config(command=self.reverse)

    def quit(self):
        self.view.master.destroy()

    def load_deck(self):
        filepath = filedialog.askopenfilename()

        if filepath and self.model.load(filepath):
            self.view.next_button.config(text="Commencer", state=NORMAL)
            self.view.reverse_button.config(state=NORMAL)
            self.view.question_label.config(text="Micro")
            self.view.answer_label.config(text="Memo")
            self.view.answer_label.pack(expand=True)

    def next_or_flip_card(self):
        if self.model.state == "FLIP" or self.model.state == "READY":
            self.model.next_card()
            self.model.state = "NO_FLIP"
            self.view.question_label.config(text=self.model.current_question())
            self.view.answer_label.config(text=self.model.current_answer())
            self.view.answer_label.pack_forget()
            self.view.next_button.config(text="Voir la réponse")
        elif self.model.state == "NO_FLIP":
            self.view.answer_label.pack(expand=True)
            self.view.next_button.config(text="Carte suivante")
            self.model.state = "FLIP"

    def reverse(self):
        self.model.set_reverse_mode(not self.model.reverse_mode)
        self.view.reverse_button.config(state=NORMAL)
        self.view.question_label.config(text="Micro")
        self.view.answer_label.config(text="Memo")
        self.view.next_button.config(text="Commencer")
        self.view.answer_label.pack(expand=True)

    def refresh(self):
        model.refresh()
