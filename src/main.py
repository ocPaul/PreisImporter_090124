import matplotlib.pyplot as plt
import csv
from datetime import datetime


class StockDataProcessor:

    def __init__(self, filename):
        self.data = self.import_data(filename)

    def import_data(self, filename):
        data = []
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                name, timestamp, price, currency, exchange = row
                timestamp = int(timestamp)
                date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                data.append({'name': name, 'date': date, 'price': float(price), 'currency': currency, 'exchange': exchange})
        return data

    def visualize_data(self):
        for stock in self.data:
            plt.plot(stock['date'], stock['price'], label=f"{stock['name']} - {stock['exchange']}")
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('Stock Prices Over Time')
        plt.legend()
        plt.show()


if __name__ == '__main__':
    processor = StockDataProcessor('./files/bums.csv')
    processor.visualize_data()
