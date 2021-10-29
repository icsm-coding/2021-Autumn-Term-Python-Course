from questionnaire_model import QuestionnaireModel
from question_data import questions_list

questionnaire = QuestionnaireModel(questions_list)

while questionnaire.has_quiz_ended() == False:
    print(f'{questionnaire.get_current_question()} Your options are:')
    options_list = questionnaire.get_current_options()
    for option in options_list:
        print(option)
    user_choice = input('Enter your choice here: ').lower()
    while not questionnaire.is_user_choice_legitimate(user_choice):
        user_choice = input('Wrong input. Please enter A, B, C or D: ').lower()
    questionnaire.increment_score(user_choice)
    questionnaire.increment_question_index()

questionnaire.get_results()
