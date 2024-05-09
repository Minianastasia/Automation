from smartphone import Smartphone

каталог = []

каталог.append(Smartphone("Apple", "iPhone 13", "+79123456789"))
каталог.append(Smartphone("Samsung", "Galaxy S21", "+79234567890"))
каталог.append(Smartphone("Xiaomi", "Mi 11", "+79345678901"))
каталог.append(Smartphone("OnePlus", "9 Pro", "+79456789012"))
каталог.append(Smartphone("Google", "Pixel 6", "+79567890123"))

for телефон in каталог:
    print(f"{телефон.марка} - {телефон.модель}. {телефон.номертелефона}")