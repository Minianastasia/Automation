

side_length = float(input("Введите длину стороны квадрата: "))

area = int(side_length) ** 2 + 1 if side_length % 1 != 0 else int(side_length) ** 2

print("Площадь квадрата со стороной", side_length, "равна", area)

