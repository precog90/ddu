import csv
import os
import statistics

from real_estate_data_miner.data_types import Purchase


def print_header(banner_name):
    """Prints header for the program."""
    print()
    print()
    print("----------------------------------------------------")
    print("                {0}".format(banner_name))
    print("-----------------------------------------------------")
    print()


def get_data_file():
    """This function returns full path of the file where data is stored"""
    base_folder = os.path.dirname(__file__)
    # print(base_folder)
    return os.path.join(base_folder, 'data', 'Sacramentorealestatetransactions.csv')
    # print(filename)


def load_file(filename):
    """This function loads the date from the filename"""
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin, delimiter=',')
        purchases = []
        for row in reader:
            # print(type(row), row)
            p = Purchase.create_from_dict(row)
            purchases.append(p)
        return purchases


def query_data(data):
    """This function queries the csv data file"""
    # Most expensive house
    # Least expensive house
    # Average Price house
    # Average Price of 2 Bedroom House
    #if data was sorted by price
    data.sort(key=lambda p: p.price)
    # for d in data:
    #     print(d.price)

    high_purchase = data[-1]
    print("The most expensive house is ${:,} is with {} beds and {} baths".format(high_purchase.price,
                                                                               high_purchase.beds,
                                                                               high_purchase.baths))

    low_purchase = data[0]
    print("The least expensive house is ${:,} is with {} beds and {} baths ".format(low_purchase.price,
                                                                                    low_purchase.beds,
                                                                                    low_purchase.baths))

    two_bedroom_homes = [
        p
        for p in data
        if p.beds == 2
    ]
    # for p in data:
    #     if p.beds == 2:
    #         prices.append(p.price)
    avg_price = statistics.mean(p.price for p in two_bedroom_homes)
    avg_baths = statistics.mean(p.baths for p in two_bedroom_homes)
    avg_sqft = statistics.mean(p.sq__ft for p in two_bedroom_homes)

    print("The average home price of a 2 Bed Room house is ${:,}, baths {}, sq ft = {}".format(int(avg_price),
                                                                                               round(avg_baths),
                                                                                               round(avg_sqft)))


def main():
    """Main Method"""
    print_header("REAL ESTATE DATA MINER APP")
    filename = get_data_file()
    data = load_file(filename)
    # print(data[0])
    query_data(data)


if __name__ == '__main__':
    main()
