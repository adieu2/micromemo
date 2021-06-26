import csv
import random

from script.constants import *

class MicroMemo:

    def __init__(self):
        self.initialize()

    def initialize(self):
        self.questions = []
        self.answers = []
        self.i = None
        self.filepath = None
        self.reverse_mode = False
        self.state = State.NO_DECK

    def count(self):
        return len(self.questions)

    def load(self, path):
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            questions = []
            answers = []

            try:
                for row in csv_reader:
                    questions.append(row[0])
                    answers.append(row[1])
            except (csv.Error, IndexError) as e:
                return False

        self.initialize()
        self.questions = questions
        self.answers = answers
        self.state = State.READY
        return True

    def set_reverse_mode(self, mode):
        self.reverse_mode = mode

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
        previous = self.i

        while (self.i == previous):
            self.i = random.randint(1, self.count()) - 1 
