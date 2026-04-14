#!pip install faker

from faker import Faker
fake = Faker('ru_RU')
print(fake.name())
print(fake.job())
