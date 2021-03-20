import random

all_data = []

for i in range(3000):
    size = random.randint(1300, 2500)
    year = random.randint(1920, 2019)
    cost = (random.randint(200000, 700000))/1000
    stories = (random.randint(1, 4))*1000
    houseType = random.choice([500, 1000, 1500, 2000, 2500, 3000])

    all_data.append([size, year, cost, stories, houseType])

print(all_data)