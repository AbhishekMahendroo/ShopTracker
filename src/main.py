import pandas as pd
from src.inventory import InventoryManager
from src.sales import SalesManager

INPUT_FILE = r"C:\Users\Abhishek Mahendroo\Documents\PythonProject\ShopSalesTracker\data\shop_inventory.xlsx"
SALES_LOG = r"C:\Users\Abhishek Mahendroo\Documents\PythonProject\ShopSalesTracker\data\daily_sales.xlsx"

def main():
    """Main function to run the shop system."""
    # Initialize managers
    inventory_manager = InventoryManager(INPUT_FILE)
    sales_manager = SalesManager()

    total_sales = []

    while True:
        print("\n1. Make a Sale\n2. Close Shop")
        choice = input("Select an option: ")

        if choice == '1':
            # Process sales
            sales = sales_manager.process_sales(inventory_manager.inventory)
            if sales:
                total_sales.extend(sales)
                total_price = sum(item['price'] for item in sales)
                sales_manager.generate_bill(sales, total_price)

        elif choice == '2':
            # Close shop and save data
            print("Shop closing. Generating report...")
            inventory_manager.update_inventory(total_sales)
            inventory_manager.save_inventory()
            sales_manager.update_sales_log(total_sales, SALES_LOG)
            print("Summary saved. See daily_sales.xlsx")
            break

        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
