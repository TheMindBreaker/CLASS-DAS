#Fernando Ruiz Velasco Hernandez
#A91229632
#28/09/2023

import csv

def read_csv_to_dict(filename):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def write_list_of_dicts_to_csv(filename, data, fieldnames):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def main(file_1, file_2, out_file):
    data_1 = read_csv_to_dict(file_1)
    data_2 = read_csv_to_dict(file_2)
    products_1 = {row['SKU']: row for row in data_1}

    for product in data_2:
        if product['SKU'] in products_1:
            products_1[product['SKU']]['Quantity'] = str(int(products_1[product['SKU']]['Quantity']) + int(product['Quantity']))
        else:
            data_1.append(product)

    fieldnames = ["SKU", "Name", "Description", "Price", "Quantity", "Expiration Date"]
    write_list_of_dicts_to_csv(out_file, data_1, fieldnames)

if __name__ == "__main__":
    main("grocery_batch_1.csv","sample_grocery.csv","grocery_db.csv")
