import pandas as pd

GST_RATE = 0.18


class SalesManager:
    """Class to manage sales operations."""

    def __init__(self, gst_rate: float = GST_RATE):
        """
        Initializes the SalesManager with a GST rate.

        Args:
            gst_rate (float): GST rate to be applied to sales.
        """
        self.gst_rate = gst_rate

    def generate_bill(self, items: list, total: float) -> None:
        """
        Generates a bill with GST.

        Args:
            items (list): List of items sold.
            total (float): Total price of the items before GST.
        """
        gst = total * self.gst_rate
        grand_total = total + gst
        print("\n---- Bill ----")
        for item in items:
            print(f"{item['name']}: {item['quantity']} - ₹{item['price']}")
        print(f"GST ({self.gst_rate * 100}%): ₹{gst:.2f}")
        print(f"Total: ₹{grand_total:.2f}\n")

    def update_sales_log(self, sales: list, file_path: str) -> None:
        """
        Logs daily sales to an Excel file.

        Args:
            sales (list): List of sales transactions.
            file_path (str): Path to the sales log Excel file.
        """
        df = pd.DataFrame(sales)
        df.to_excel(file_path, index=False)

    def process_sales(self, df: pd.DataFrame) -> list:
        """
        Handles sales transactions for the day.

        Args:
            df (pd.DataFrame): DataFrame containing inventory data.

        Returns:
            list: List of sales transactions.
        """
        sales = []
        while True:
            item_name = input("Enter product name (or 'exit' to stop): ").strip()
            if item_name.lower() == "exit":
                break

            if item_name not in df["name"].values:
                print("Item not found!")
                continue

            quantity = float(input("Enter quantity: "))
            product = df[df["name"] == item_name].iloc[0]
            if quantity > product["quantity"]:
                print("Not enough stock!")
                continue

            price = product["price"] * quantity
            sales.append({"name": item_name, "quantity": quantity, "price": price})

        return sales
