class Shop():
    def __init__(self, object , price , title):
        self.object = object 
        self.price = price 
        self.title = title

    def get_info(self):
        print(self.object)
        print(self.price)
        print(self.title)


class Films(Shop):

    def get_info(self):
        print(self.object)
        print(self.price)
        print(self.title)


class Book(Shop):

    def get_info(self):
        print(self.object)
        print(self.price)
        print(self.title)

class Products(Shop):


    def add_products(self , shop , *products):
        for prod in products:
            shop.append(prod)

    def print_products(self , shop):
        for prod in shop:
            print(shop)

shop = []

film_1 = Shop("Фильм", 1000 , "Kinkong \n")
film_2 = Shop("Фильм", 300 , "Unforgiven \n")
film_3 = Shop("Фильм", 289 , "Argument \n")
film_4 = Shop("Фильм", 1238 , "Dune \n")
film_5 = Shop("Фильм", 6789 , "I_going_to_look \n")
film_2.get_info()
film_4.get_info()

book_1 = Shop("Книга", 49 , "witcher \n")
book_2 = Shop("Книга", 44 , "anxious_people \n")
book_3 = Shop("Книга", 23 , "inside_the_killer \n")
book_4 = Shop("Книга", 67 , "Metro \n")
book_5 = Shop("Книга", 11 , "morphine \n")
book_1.get_info()
book_3.get_info()

people_inquiry = input("Что вы хотите купить ?: ")
basket = people_inquiry
print("Вы добавили в корзину" , basket)











