from operator import ge


class Film():

    def __init__(self , director, title , year):
        self.director = director
        self.title = title
        self.year = year
    
    def get_info(self):
        print(self.director)
        print(self.title)
        print(self.year)


film_1 = Film('Rawsom_marshall' , 'red_notice' , 2021 )
print("Первый фильм:")
film_1.get_info()

film_2 = Film('Andy_Serkis' , 'venom_2' , 2021)
print("Второй фильм:")
film_2.get_info()

film_3 = Film('Cary_Fukunaga' ,'No_time_to_die', 2021)
print("Третий фильм:")
film_3.get_info()