#!pip install faker

from faker import Faker
fake = Faker('en_US')
print(fake.email())
print(fake.job())
