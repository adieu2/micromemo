from tkinter import *
from tkinter import filedialog, messagebox

from script.constants import *

class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.configure_events(view)

    def configure_events(self, view):
        view.load_button.config(command=self.load_button)
        view.next_button.config(command=self.next_button)
        view.reverse_button.config(command=self.reverse_button)

    def load_button(self):
        filepath = filedialog.askopenfilename()
        if not filepath: return

        if self.model.load(filepath):
            self.view.get_ready("Micromemo")
            messagebox.showinfo("Cards loaded", "{} cards loaded".format(self.model.count()))
        else:
            messagebox.showinfo("Error", "Could not load .csv file {}".format(filepath))

    def next_button(self):
        if self.model.state == State.CARD_FLIPPED or self.model.state == State.READY:
            self.model.next_card()
            self.model.state = State.CARD_HIDDEN
            self.view.prompt_question(self.model.current_question(), self.model.current_answer())
        elif self.model.state == State.CARD_HIDDEN:
            self.view.show_answer()
            self.model.state = State.CARD_FLIPPED

    def reverse_button(self):
        self.model.set_reverse_mode(not self.model.reverse_mode)
        self.model.state = State.READY
        self.view.get_ready(message="All cards were flipped")
