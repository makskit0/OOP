class Credit():
    def __init__(self , full_name , age , gender , income , credit_history , sum):
        self.full_name = full_name
        self.age = age
        self.gender = gender
        self.income = income
        self.credit_history = credit_history
        self.sum = sum

    def get_info(self):
        print(self.full_name)
        print(self.age)
        print(self.gender)
        print(self.income )
        print(self.credit_history)
        print(self.sum)

    def condition(self , points):
        points = 0
        if  21 < self.age < 40:
            points = +10
        elif self.age > 40:
            points = +20
        if self.gender == "female":
            points = +10
        if 20000 < self.income < 40000:
            points = +10
        elif self.income > 40000:
            points = +20
        if self.credit_history == "Да":
            points = +20
        if sum < 20000:
            points = +20
        elif 20000 < self.sum <40000:
            points = +10
        print("У вас", points, "баллов!")
        if points >= 50:
            print("Мы можем выдать вам этот кредит!")
        else:
            print("В кредите отказано!")
        

people_1 = Credit(input("Ваше имя: "),input("Ваш возраст: "), input("Ваш пол: "),input("Ваше доход: "),input("Есть кридитная история ?: "),input("Жлелаемая сумма ?: ") )
people_1.get_info()
people_1.condition()