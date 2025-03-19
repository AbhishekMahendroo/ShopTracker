import pandas as pd
from src.inventory import load_inventory, save_inventory, update_inventory
from src.sales import process_sales, generate_bill, update_sales_log

INPUT_FILE = "data/shop_inventory.xlsx"
SALES_LOG = "data/daily_sales.xlsx"


def main():
    """Main function to run the shop system."""
    inventory = load_inventory(INPUT_FILE)
    total_sales = []

    while True:
        print("\n1. Make a Sale\n2. Close Shop")
        choice = input("Select an option: ")

        if choice == '1':
            sales = process_sales(inventory)
            if sales:
                total_sales.extend(sales)
                total_price = sum(item['price'] for item in sales)
                generate_bill(sales, total_price)

        elif choice == '2':
            print("Shop closing. Generating report...")
            inventory = update_inventory(inventory, total_sales)
            update_sales_log(total_sales, SALES_LOG)
            save_inventory(inventory, INPUT_FILE)
            print("Summary saved. See daily_sales.xlsx")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
