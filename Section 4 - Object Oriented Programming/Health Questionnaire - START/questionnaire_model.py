from question_model import QuestionModel


class QuestionnaireModel:
    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.current_question_index = 0
        self.question_objects_list = self.get_question_objects()
        self.user_score = 0

    def get_question_objects(self):
        question_objects_list = []
        for question_dict in self.questions_list:
            question_objects_list.append(
                QuestionModel(question=question_dict['question'], options=question_dict['options']))
        return question_objects_list

    def has_quiz_ended(self):
        if self.current_question_index >= len(self.question_objects_list):
            return True
        else:
            return False

    def get_current_question(self):
        return self.question_objects_list[self.current_question_index].question

    def get_current_options(self):
        return self.question_objects_list[self.current_question_index].options

    def increment_question_index(self):
        self.current_question_index += 1

    def increment_score(self, user_choice):
        if user_choice == 'A':
            self.user_score += 0
        if user_choice == 'B':
            self.user_score += 1
        if user_choice == 'C':
            self.user_score += 2
        if user_choice == 'D':
            self.user_score += 3

    def is_user_choice_legit(self, user_choice):
        if user_choice in ['A', 'B', 'C', 'D']:
            return True
        else:
            return False

    def get_result(self):
        if self.user_score <= 5:
            return f'Your score was {self.user_score} out of 15. You are really unhealthy. Sort your life out!'
        elif 5 < self.user_score <= 10:
            return f'Your score was {self.user_score} out of 15. Your health is mediocre at best. Sort your life out!'
        else:
            return f'Your score was {self.user_score} out of 15. Your health is too good. Drink some mountain dew!'
