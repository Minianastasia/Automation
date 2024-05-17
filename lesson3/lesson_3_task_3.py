from address import Address
from mailing import Mailing

# Создаем адреса
to_address = Address("123456", "Москва", "Ленина", "10", "25")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "5", "10")

# Создаем почтовое отправление
mailing = Mailing(to_address, from_address, 250, "ABC123456789")

# Выводим информацию о почтовом отправлении
print(f"Отправление {mailing.track} из {mailing.from_address.индекс}, {mailing.from_address.город}, {mailing.from_address.улица}, {mailing.from_address.дом} - {mailing.from_address.квартира} в {mailing.to_address.индекс}, {mailing.to_address.город}, {mailing.to_address.улица}, {mailing.to_address.дом} - {mailing.to_address.квартира}. Стоимость {mailing.cost} рублей.")