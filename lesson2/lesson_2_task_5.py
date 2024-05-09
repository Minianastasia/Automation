month_number = int(input("Введите номер месяца: "))

def month_to_season(month):
    if month in [12, 1, 2]:
        return "Зима"
    if month in [3, 4, 5]:
        return "Весна"
    if month in [6, 7, 8]:
        return "Лето"
    if month in [9, 10, 11]:
        return "Осень"
    return "Неверный номер месяца"


season = month_to_season(month_number)
print(f" {season}")
