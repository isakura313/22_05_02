from Survey import AnonimSurvey


#определяет вопрос, и сохраняет все ответы
question = "Какой язык вы хотите изучать первым"
my_survey = AnonimSurvey(question)

#показываем вопрос и сохраняем ответ
my_survey.show_question()
print("Введите 'q' для окончания работы программы")
while True:
    response = input('Язык \n')
    if response == 'q':
        break
    my_survey.store_response(response)


#показываем результаты опроса
print("Спасибо! ")
my_survey.show_results()