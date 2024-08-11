# This file is to explain how to use comma seperated(CSV)  values in python 
import csv

class ItemStore:
    def __init__(self, item_name: str, price: float, quantity: int):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity

    def to_csv_table_format(self) -> str:
        return f"{self.item_name}, {self.price}, {self.quantity}"

class CsvExtractor:
    @classmethod
    def create_csv(cls) -> None:
        try:
            with open('items.csv', 'x') as f:
                store_table_title = "Item, Price, Quantity"
                f.write(store_table_title + '\n')
        except FileExistsError:
            print('File already exists')

    @classmethod
    def read_csv(cls) -> list[dict[str, str]]:
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        return items

    @classmethod
    def write_csv(cls) -> None:
        store_item_name = input("Input item name: ")
        store_item_price = float(input("Input item price in decimal: "))
        store_item_quantity = int(input("Input item quantity in integer: "))
        item = ItemStore(item_name=store_item_name, price=store_item_price, quantity=store_item_quantity)
        with open('items.csv', 'a') as f:
            f.write(item.to_csv_table_format() + '\n')



        
            

        



#  creates csv file 
CsvExtractor.create_csv()

# write to csv

CsvExtractor.write_csv()

# read csv file 
print(CsvExtractor.read_csv())



