class credit():
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

points = 0
full_name = input("Введите ФИО: ")
age = int(input("Введите возраст: "))
gender = input("Введите пол: ")
income = int(input("Введите доход в месяц: "))
credit_history = input("У вас есть кридитная история ?: ")
sum = int(input("Введите сумму , которую хотите получить: "))
if  21 < age < 40:
    points = +10
elif age > 40:
    points = +20
if gender == "female":
    points = +10
if 20000 < income < 40000:
    points = +10
elif income > 40000:
    points = +20
if credit_history == "Да":
    points = +20
if sum < 20000:
    points = +20
elif 20000 < sum <40000:
    points = +10
print("У вас", points, "баллов!")
if points >= 50:
    print("Мы можем выдать вам этот кредит!")
else:
    print("В кредите отказано!")