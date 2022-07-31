# 13.07.2022 
# Inkapsulyatsiya va klassga oid xususiyat va metodlar
# Muallif: Shaxzodjon Zoirov

# Inkapsulyatsiya bu - biron bir obyektni yashirish uchun ishlatiladi va tashqaridan yopish uchun xizmat qiladi
#



from uuid import uuid4
class Avto:
    """Avtomobil klassi"""
    def __init__(self,make, model,rang, yil, narh, km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()

    def get_km(self):
        # bu yerda bizga kmni olib beradi.
        return self.__km
    def get_id(self):
        # idsini olib beradi
        return self.__id

    def add_km(self,km):
        """Mashinaning km ga yana km qo'shuvchi metod"""
        if km>=0:
          self.__km += km
        else:
            print("Mashina km ga kamayib borishi")
            
# Inkapsulyatsiya va klassga oid xususiyat va metodlar

# Inkapsulyatsiya bu - biron bir obyektni yashirish uchun ishlatiladi va tashqaridan yopish uchun xizmat qiladi


from uuid import uuid4
class Avto:
    """Avtomobil klassi"""
    def __init__(self,make, model,rang, yil, narh, km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()

    def get_km(self):
        # bu yerda km ni olib beradi.
        return self.__km
    def get_id(self):
        # id sini olib beradi
        return self.__id

    def add_km(self,km):
        """Mashinaning km ga yana km qo'shuvchi metod"""
        if km>=0:
          self.__km += km
        else:
            print("Mashina km ga kamayib borishi")