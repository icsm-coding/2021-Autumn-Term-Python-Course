from questionnaire_model import QuestionnaireModel
from question_data import questions_list

questionnaire = QuestionnaireModel(questions_list=questions_list)

while questionnaire.has_quiz_ended() == False:
    print(questionnaire.get_current_question())
    options_list = questionnaire.get_current_options()
    for option in options_list:
        print(option)
    user_choice = input('What is your choice: A, B, C or D? ')
    while questionnaire.is_user_choice_legit(user_choice=user_choice) == False:
        user_choice = input('Wrong input. What is your choice: A, B, C or D? ')
    questionnaire.increment_score(user_choice=user_choice)
    questionnaire.increment_question_index()

print(questionnaire.get_result())


class Phone:
    def __init__(self):
        self.batter_percentage = 0


def charge_battery(self):
    self.battery_percentage += 10


