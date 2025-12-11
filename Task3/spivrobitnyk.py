class Spivrobitnyk:
    def __init__(self, imya, zarplata, vidprac_dni, vidsotok_bonus=0):
        self._imya = imya
        self._zarplata = zarplata
        self._vidprac_dni = vidprac_dni
        self._vidsotok_bonus = vidsotok_bonus

    # Гетери
    def get_imya(self):
        return self._imya

    def get_zarplata(self):
        return self._zarplata

    def get_vidprac_dni(self):
        return self._vidprac_dni

    def get_vidsotok_bonus(self):
        return self._vidsotok_bonus

    # Сетери
    def set_imya(self, imya):
        self._imya = imya

    def set_zarplata(self, zarplata):
        self._zarplata = zarplata

    def set_vidprac_dni(self, dni):
        self._vidprac_dni = dni

    def set_vidsotok_bonus(self, vidsotok):
        self._vidsotok_bonus = vidsotok

    # Метод для розрахунку місячної зарплати
    def rozrahunok_zarplaty(self):
        return (self._zarplata / 30) * self._vidprac_dni

    # Метод для розрахунку бонусу
    def rozrahunok_bonus(self):
        return (self.rozrahunok_zarplaty() / 100) * self._vidsotok_bonus