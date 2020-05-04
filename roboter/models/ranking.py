import csv
import os
import pathlib

class Csv(object):
    def __init__(self,csv_filename=''):
        self.csv_path = os.getcwd() + '/csv/'
        self.field_names = ['Name', 'Count']
        self.csv_filename = csv_filename

    def make_csv(self):
        """ Make csv file & write field header
        """
        if not(os.path.exists(self.csv_filename)):
            pathlib.Path(self.csv_filename).touch()
            with open(self.csv_filename, 'w') as csv_file:
                writer = csv.DictWriter(csv_file, self.field_names)
                writer.writeheader()

    def read_csv(self):
        """ Return dictionary of csv data
        :return:
            Dictionary of csv data
        """
        d_restaurant = {}
        with open(self.csv_filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                d_restaurant[row['Name']] = int(row['Count'])
        return d_restaurant

    def write_csv(self, d_restaurant):
        """ Create csv file
        :param
            d_restaurant: Dictionary of csv data
        """
        with open(self.csv_filename, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.field_names)
            writer.writeheader()
            for k, v in d_restaurant.items():
                writer.writerow({'Name': k, 'Count': v})

class RankingCsv(Csv):
    def __init__(self):
        super().__init__()
        self.csv_filename = self.csv_path + 'ranking.csv'
        super().make_csv()

    def add_restaurant(self, restaurant_name):
        """ Add restaurant data to csv file"""
        d_restaurant = self.read_csv()
        if restaurant_name in d_restaurant:
            d_restaurant[restaurant_name] += 1
        else:
            d_restaurant[restaurant_name] = 1

        self.write_csv(d_restaurant)