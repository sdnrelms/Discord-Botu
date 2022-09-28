from random import randint as r

class Game:

    @staticmethod
    def küçük_sayı():
        return r(1, 100)


    @staticmethod
    def büyük_sayı():
        return r(100, 1000)