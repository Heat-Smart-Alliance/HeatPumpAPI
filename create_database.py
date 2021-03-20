import random
from faker import Faker

faker = Faker()

all_data = []

for i in range(3000):
    id = faker.uuid4()
    name = faker.name()
    email = faker.email()
    size = random.randint(1300, 2500)
    year = random.randint(1920, 2019)
    cost = (random.randint(200000, 700000))/1000
    stories = (random.randint(1, 4))*1000
    houseType = random.choice([500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500])

    all_data.append([id, name, email, size, year, cost, stories, houseType])

print(all_data)