from tkinter.messagebox import QUESTION


class Quiz():
    def __init__(self , question , answer):
        self.question = question
        self.answer = answer

    def get_info(self):
        print(self.question)
        print(self.answer)

    def your_answer(self):
        user_answer = input("Введите ответ: ")    
        if user_answer == true_answer:
            print("Это верный ответ!") 

true_answer = {

    "Начало Второй Мировой Войны ?" : 1939,
    "два плюс два " : 4,
    "корень из 25 " : 5,
    "английский перевод слова вопрос " : "question"
}

question_1 = Quiz("Начало Второй Мировой Войны ?" , 1939)
question_2 = Quiz("два плюс два ?" , 4 )
question_3 = Quiz("корень из 25 " , 5)
question_4 = Quiz("английский перевод слова вопрос " , "question")

print(question_1.question)
print(question_1.your_answer())
print(question_1.answer)