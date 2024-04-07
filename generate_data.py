import csv
from faker import Faker
import random

fake = Faker()

# Define departments
departments = ['HR', 'Finance', 'Engineering', 'R&D']

# Generate data for 100 employees as an example
num_employees = 100

with open('database.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Hiring Date', 'Department', 'Birthday'])
    for _ in range(num_employees):
        name = fake.name()
        hiring_date = fake.date_between(start_date='-10y', end_date='today')
        department = random.choice(departments)
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=60).strftime('%Y-%m-%d')
        writer.writerow([name, hiring_date, department, birthday])
