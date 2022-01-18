
class Quiz():
    def __init__(self , question , answer , score):
        self.question = question
        self.answer = answer
        self.score = score

    def ask_question(self):
        print(question_1)
        print(question_2)
        print(question_3)
        print(question_4)

    def check_the_answer(self):
        if user_answer == question_and_answer["Начало Второй Мировой Войны ?"]:
            print("Верный ответ!")
            self.score += 1
        else:
            print(question_and_answer)


question_and_answer = {
    "Начало Второй Мировой Войны ?" : 1939,
    "два плюс два ?" : 4 ,
    "корень из 25 ?" : 5,
    "английский перевод слова вопрос ?" : "question"
    
}
score = 0
question = Quiz()
print(question.ask_question())
user_answer = input("Введите ваш ответ:")
check_answer = Quiz()
check_answer.check_the_answer()
question_1 = ("Начало Второй Мировой Войны ?" )
question_2 = ("два плюс два ?" )
question_3 = ("корень из 25 ? " )
question_4 = ("английский перевод слова вопрос ? " )

