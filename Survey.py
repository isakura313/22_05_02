class AnonimSurvey:
    """ Собирает анонимные ответы на вопрос"""
    def __init__(self,question):
        """ Содержит вопрос, и подготавливает ответ"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Показать вопрос"""
        print(self.question)

    def store_response(self, new_response):
        """Сохраняет имеющийся в нас ответ"""
        if new_response == '':
            return
        self.responses.append(new_response)

    def show_results(self):
        """ Показывает все ответы, которые должны быть даны"""
        print("Итоги опроса показали следующее: \n")
        for response in self.responses:
            print(f" = {response}")