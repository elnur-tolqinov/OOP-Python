# Klasslar

# x=10
# print(type(x))
# matn="salom"
# print(type(matn))
# print(matn.upper())



# def salom():
#     print("Assalom alekum")

# print(type(salom))


class Talaba:
    # Talaba degan klass yaratildi
    def __init__(self, ism,familiya,tyil):
        # va uning ichiga def __init__ orqali  hususiyatlar qo'shadi
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
#talaba1, talaba2, va talaba3 degan o'zgaruvchilarga ma'lumot saqlaymiz.
talaba1 = Talaba("Olim,", "Olimov",2000)
talaba2 = Talaba("Hasan,", "Hakimov",1994)
talaba3 = Talaba("Husan,", "Hasanov",2004)




