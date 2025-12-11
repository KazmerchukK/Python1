from spivrobitnyk import Spivrobitnyk

class Menedzher(Spivrobitnyk):
    _rozmir_premiyi = 500  # Статичний атрибут для всіх менеджерів

    def __init__(self, imya, zarplata, vidprac_dni, kilkist_pidleglyh, vidsotok_bonus=0):
        super().__init__(imya, zarplata, vidprac_dni, vidsotok_bonus)
        self._kilkist_pidleglyh = kilkist_pidleglyh

    # Гетери і сетери
    def get_kilkist_pidleglyh(self):
        return self._kilkist_pidleglyh

    def set_kilkist_pidleglyh(self, kilkist):
        self._kilkist_pidleglyh = kilkist

    # Метод для звіту
    def zvit(self):
        return f"Менеджер {self._imya} керує {self._kilkist_pidleglyh} співробітниками."

    # Перевизначення методу бонусу
    def rozrahunok_bonus(self):
        bazovyi_bonus = super().rozrahunok_bonus()
        return bazovyi_bonus + (self._kilkist_pidleglyh * Menedzher._rozmir_premiyi)