import csv
import random

products = ['rye bread', 'wheat bread', 'oil', 'flour', 'pumpkin', 'cheese', 'butter',
            'cream', 'yoghurt', 'eggs', 'beef', 'pork', 'mutton', 'chicken',
            'sausage', 'ham', 'shrimps', 'chocolate', 'caramels', 'cookies']

items = [sorted(random.sample(products, random.randint(2, 5))) for _ in range(1000)]
items.sort()

with open('order_bd.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for item in items:
        writer.writerow(item)