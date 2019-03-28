from builtins import print

import QuestionStore
from CustomException import QuestionPaperCanNotBeGenerated, QuestionPaperCanNotBeCreatedWithFractionMarks
from Question import Question
from QuestionStore import QuestionStore


class QuestionServices:
    total_que = None

    def __init__(self, file_path):
        self.file_path = file_path
        self.no_of_ques = 0

    def populate_question_store(self):
        f = open(self.file_path, 'r')

        for line in f.readlines():
            line_arr = line.split(", ")

            question_obj = Question(line_arr[0], line_arr[1], line_arr[2])

            self.save_question(question_obj)

            self.no_of_ques += 1

    @staticmethod
    def save_question(question):
        QuestionStore.question_list.append(question)

    @staticmethod
    def get_question_paper(configuration):

        total = configuration["total"]

        del configuration['total']

        que_distribution = configuration

        paper = []

        for difficulty in que_distribution:
            ques_list_for_level = QuestionServices.get_ques_for_level(total, difficulty, que_distribution.get(difficulty))

            for x in ques_list_for_level:
                paper.append(x)
        return paper

    @staticmethod
    def get_ques_for_level(total_marks, difficulty, difficulty_marks):
        list_of_all_que_with_level = []

        total_marks_for_level = (difficulty_marks * total_marks) / 100

        for que in QuestionStore.question_list:
            if que.get_level() == difficulty:
                list_of_all_que_with_level.append(que)

        list_of_all_que_with_level = sorted(list_of_all_que_with_level, key=lambda question: question.marks, reverse=True)

        final_list_of_que = QuestionServices.get_sub_list(list_of_all_que_with_level, total_marks_for_level)
        if len(final_list_of_que) == 0:
                    raise QuestionPaperCanNotBeGenerated
        return final_list_of_que

    def get_sub_list(list, target):

        target = target
        que_list = []

        for que in list:
            if target == 0:
                break
            elif type(target)(que.get_marks()) <= target:
                que_list.append(que.get_question_id())
                target -= type(target)(que.get_marks())

        if target < 0:
            raise QuestionPaperCanNotBeGenerated

        return que_list
