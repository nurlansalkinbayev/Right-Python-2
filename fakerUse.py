from faker import Faker
import csv

# Создаем экземпляр Faker
fake = Faker()

# Открываем файл для записи данных
with open('fake_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Email', 'Phone']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    # Генерируем и записываем данные в файл
    for _ in range(100):
        writer.writerow({'Name': fake.name(), 'Email': fake.email(), 'Phone': fake.phone_number()})
