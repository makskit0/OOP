class Money():
    def __init__(self , usd , rub , euro):
        self.usd = usd
        self.rub = rub
        self.euro = euro

value = input("Введите валюту  которую хотите купить: ")
if value == 'usd':
    usd = int(input("Сколько долларов вы хотите купить ?: "))
    rub = usd * 70 
    print("К оплате " , rub , "rub")
elif value == 'euro':
    euro = int(input("Сколько евро вы хотите купить ?: "))
    rub = euro * 87
    print("К оплате " , rub , "rub")
else:
    print("Такой валюты не существует!!")