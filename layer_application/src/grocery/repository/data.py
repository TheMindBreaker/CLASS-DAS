import csv
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), 'sample_grocery.csv')
FIELDS = ['SKU', 'Name', 'Description', 'Price', 'Quantity', 'Expiration Date']


def load_data():
    with open(DATA_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

def load_sku(sku):
    data = load_data()
    for item in data:
        if item['SKU'] == sku:
            return item
    return None

def add_item(item):
    data = load_data()
    for product in data:
        if product['SKU'] == item['SKU']:
            return False
    print(item)
    with open(DATA_FILE, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writerow({value: item.get(value, '') for value in FIELDS})
    return True


def delete_item_by_sku(sku):
    data = load_data()
    item_exists = any(item['SKU'] == sku for item in data)

    if not item_exists:
        return False

    with open(DATA_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            if row['SKU'] != sku:
                writer.writerow(row)
    return True
