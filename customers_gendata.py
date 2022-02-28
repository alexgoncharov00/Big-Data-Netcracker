import numpy as np
import pandas as pd
import csv

data_size = 10000                      # задание объема данных


def gen_id(num):
    num = str(num)
    while len(num) < len(str(data_size)):
        num = '0' + num
    return num


def gen_first_name(gender):
    male_names = ['Jose', 'Joao', 'Antonio', 'Francisco', 'Carlos', 'Paulo',
                  'Pedro', 'Lucas', 'Luiz', 'Marcos']
    female_names = ['Maria', 'Ana', 'Franciska', 'Antonia', 'Andriana', 'Juliana',
                    'Marcia', 'Fernanda', 'Patricia', 'Aline']
    if gender == 'male':
        return np.random.choice(male_names)
    else:
        return np.random.choice(female_names)


def gen_last_name():
    last_names = ['Silva', 'Santos', 'Sousa', 'Oliveira', 'Pereira', 'Lima', 'Carvalho',
                  'Ferreira', 'Rodrigues', 'Almeida', 'Costa', 'Gomes', 'Martins',
                  'Araujo', 'Melo', 'Barbosa', 'Alves', 'Ribeiro', 'Cardoso']
    return np.random.choice(last_names)


def gen_date_of_birth():
    month = np.random.randint(1, 13)
    if month == 2:
        day = np.random.randint(1, 29)
    elif month in [4, 6, 9, 11]:
        day = np.random.randint(1, 31)
    else:
        day = np.random.randint(1, 32)
    day = str(day)
    if len(day) == 1:
        day = '0' + day
    month = str(month)
    if len(month) == 1:
        month = '0' + month
    first_part = np.random.normal(loc=20, scale=5, size=100)
    second_part = np.random.normal(loc=36, scale=20, size=1000)
    third_part = np.random.normal(loc=55, scale=20, size=300)
    age_distribution = np.concatenate([first_part, second_part, third_part])
    age_distribution = age_distribution[(age_distribution < 100) & (age_distribution >= 18)]
    year = 2022 - int(np.random.choice(age_distribution))
    return str(day) + '.' + str(month) + '.' + str(year)


def gen_promo_agreement(date_of_birth):
    age = 2022 - int(date_of_birth[-4:])
    if age < 25:
        return np.random.choice(['Yes', 'No'], p=[0.6, 0.4])
    elif age < 30:
        return np.random.choice(['Yes', 'No'], p=[0.4, 0.6])
    elif age < 40:
        return np.random.choice(['Yes', 'No'], p=[0.2, 0.8])
    elif age < 50:
        return np.random.choice(['Yes', 'No'], p=[0.05, 0.95])
    else:
        return 'No'



columns = ['Customer_ID', 'First name', 'Last name', 'date of birth',        # колонки в таблице
           'gender', 'agree_for_promo', 'autopay_card', 'email', 'MSISDN',
           'Status', 'customer category', 'customer_since', 'region',
           'language', 'termination_date']


with open("customers_data.csv", "w") as file:           # создание csv файла с заданными колонками
    writer = csv.writer(file, lineterminator='\r')
    writer.writerow(columns)


for i in range(data_size):                              # заполнение таблицы данными
        with open('customers_data.csv', 'a') as file:
            writer = csv.writer(file, lineterminator='\r')
            ID = gen_id(i + 1)
            gender = np.random.choice(['male', 'female'])
            f_name = gen_first_name(gender)
            l_name = gen_last_name()
            date_of_birth = gen_date_of_birth()
            agree_for_promo = gen_promo_agreement(date_of_birth)
            card = ''
            email = f_name.lower() + '.' + l_name.lower() + date_of_birth[-2:] + '@gmail.com'
            writer.writerow(
                [ID, f_name, l_name, date_of_birth, gender, agree_for_promo, card, email]
            )
