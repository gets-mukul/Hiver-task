class Question:
    
    def __init__(self, question_id, difficulty_level, marks):
        self.question_id = question_id
        self.level = difficulty_level
        self.marks = marks

    def get_question_id(self):
        return self.question_id

    def set_question_id(self, x):
        self.question_id = x

    def get_level(self):
        return self.level

    def set_level(self, x):
        self.level = x

    def get_marks(self):
        return self.marks

    def set_marks(self, x):
        self.marks = x