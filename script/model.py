import csv
import random

class MicroMemo:

    def __init__(self):
        self.initialize()

    def initialize(self):
        self.questions = []
        self.answers = []
        self.i = None
        self.filepath = None
        self.reverse_mode = False
        self.state = "NO_DECK_LOADED" # ["NO_DECK_LOADED", "READY", "FLIP", "NO_FLIP"]

    def count(self):
        return len(self.questions)

    def load(self, path):
        self.initialize()

        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")

            for row in csv_reader:
                self.questions.append(row[0])
                self.answers.append(row[1])

        self.state = "READY"
        return True

    def set_reverse_mode(self, mode):
        self.reverse_mode = mode

    def refresh(self):
        self.load(self.filepath)

    def has_file_loaded(self):
        return self.filepath is not None

    def current_answer(self):
        if self.reverse_mode:
            return self.questions[self.i]
        else:
            return self.answers[self.i]

    def current_question(self):
        if not self.reverse_mode:
            return self.questions[self.i]
        else:
            return self.answers[self.i]

    def next_card(self):
       self.i = random.randint(1, self.count()) - 1 
