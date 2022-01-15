class Kart():

    def __init__(self , full_name , gender , date_birth, address , disease):
        self.full_name = full_name
        self.gender = gender
        self.date_birth = date_birth
        self.address = address
        self.disease = disease

    def get_info(self):
        print(self.full_name)
        print(self.gender)
        print(self.date_birth)
        print(self.address)
        print(self.disease)



kart_1 = Kart('Kovalev_M_D' , 'male' , 1987 , 'Westminster Avenue' ,'Allergy')
print("Первый пациент:")
kart_1.get_info()
kart_2 = Kart('Labanov_K_C' , 'male' , 1967 , 'Oregon' ,'Stroke')
print("Второй пациент:")
kart_2.get_info()
kart_3 = Kart('Letamiv_L_M' , 'male' , 1987 , 'Mississippi' ,'Mumps') 
print("Третий пациент:")
kart_3.get_info()
kart_4 = Kart('Kyrochkin_H_B' , 'male' , 1999 , 'Indiana' ,'Influenza') 
print("Четвертый пациент:")
kart_4.get_info()
kart_5 = Kart('Makarov_F_N' , 'male' , 1987 , 'Florida' ,'Rabies') 
print("Пятый пациент:")
kart_5.get_info() 