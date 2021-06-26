from tkinter import *
from tkinter import filedialog, messagebox

class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.configure_events(view)

    def configure_events(self, view):
        view.load_button.config(command=self.load_button)
        view.next_button.config(command=self.next_button)
        view.reverse_button.config(command=self.reverse_button)

    def quit(self):
        self.view.master.destroy()

    def load_button(self):
        filepath = filedialog.askopenfilename()

        if filepath and self.model.load(filepath):
            self.view.next_button.config(text="Start", state=NORMAL)
            self.view.reverse_button.config(state=NORMAL)
            self.view.question_label.config(text="Micromemo")
            self.view.answer_label.config(text="Click « Start »")
            self.view.answer_label.pack(expand=True)
            messagebox.showinfo("Cards loaded", "{} cards loaded".format(self.model.count()))

    def next_button(self):
        if self.model.state == "FLIP" or self.model.state == "READY":
            self.model.next_card()
            self.model.state = "NO_FLIP"
            self.view.question_label.config(text=self.model.current_question())
            self.view.answer_label.config(text=self.model.current_answer())
            self.view.answer_label.pack_forget()
            self.view.next_button.config(text="Show answer")
        elif self.model.state == "NO_FLIP":
            self.view.answer_label.pack(expand=True)
            self.view.next_button.config(text="Next card")
            self.model.state = "FLIP"

    def reverse_button(self):
        self.model.set_reverse_mode(not self.model.reverse_mode)
        self.model.state = "READY"
        self.view.reverse_button.config(state=NORMAL)
        self.view.question_label.config(text="All cards were flipped")
        self.view.answer_label.config(text="Click « Start »")
        self.view.next_button.config(text="Start")
        self.view.answer_label.pack(expand=True)
