def bank():
    X = float(input("Введите сумму вклада: "))
    Y = int(input("Введите количество лет: "))
    return X * (1 + 0.10) ** Y, Y


result, Y = bank()
print(f"Через {Y} лет сумма на счету будет: {result:.2f} рублей")

