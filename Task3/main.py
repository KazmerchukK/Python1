from spivrobitnyk import Spivrobitnyk
from menedzher import Menedzher

spiv1 = Spivrobitnyk("Катя", 60000, 28, 10)
spiv2 = Spivrobitnyk("Марія", 25000, 30, 5)
men1 = Menedzher("Іван", 40000, 30, 5, 15)
men2 = Menedzher("Яна", 45000, 28, 8, 20)

spivrobitnyky = [spiv1, spiv2, men1, men2]

for s in spivrobitnyky:
    print(f"\nІм'я: {s.get_imya()}")
    print(f"Місячна зарплата: {s.rozrahunok_zarplaty():.2f} грн")
    print(f"Бонус: {s.rozrahunok_bonus():.2f} грн")
    if isinstance(s, Menedzher):
        print(s.zvit())