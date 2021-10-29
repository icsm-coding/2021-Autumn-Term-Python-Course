from question_model import QuestionModel


class QuestionnaireModel:

    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.current_question_index = 0
        self.user_score = 0
        self.question_objects_list = self.get_question_objects()

    def get_question_objects(self):
        question_objects_list = []
        for question_dict in self.questions_list:
            question_objects_list.append(QuestionModel(question=question_dict['question'], options=question_dict['options']))
        return question_objects_list

    def increment_question_index(self):
        self.current_question_index += 1

    def has_quiz_ended(self):
        if self.current_question_index >= len(self.questions_list):
            return True
        else:
            return False

    def get_current_question(self):
        return self.question_objects_list[self.current_question_index].question

    def get_current_options(self):
        return self.question_objects_list[self.current_question_index].options

    def increment_score(self, user_answer):
        if user_answer == 'a':
            self.user_score += 0
        elif user_answer == 'b':
            self.user_score += 1
        elif user_answer == 'c':
            self.user_score += 2
        elif user_answer == 'd':
            self.user_score += 3

    def is_user_choice_legitimate(self, user_choice):
        if user_choice not in ['a', 'b', 'c', 'd']:
            return False
        else:
            return True

    def get_results(self):
        print('\n*** Results ***\n')
        if self.user_score <= 5:
            print('You are incredibly unhealthy. Sort your life out!')
        elif 5 < self.user_score < 10:
            print('You\'re health is mediocre at best! Improve it!')
        else:
            print('You are so healthy! I wish I was you!')
        print('\n*** Results ***')