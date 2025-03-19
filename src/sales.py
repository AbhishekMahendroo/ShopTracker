import pandas as pd

GST_RATE = 0.18


def generate_bill(items: list, total: float) -> None:
    """Generates a bill with GST."""
    gst = total * GST_RATE
    grand_total = total + gst
    print("\n---- Bill ----")
    for item in items:
        print(f"{item['name']}: {item['quantity']} - ₹{item['price']}")
    print(f"GST (18%): ₹{gst:.2f}")
    print(f"Total: ₹{grand_total:.2f}\n")


def update_sales_log(sales: list, file_path: str) -> None:
    """Logs daily sales to an Excel file."""
    df = pd.DataFrame(sales)
    df.to_excel(file_path, index=False)


def process_sales(df: pd.DataFrame) -> list:
    """Handles sales transactions for the day."""
    sales = []
    while True:
        item_name = input("Enter product name (or 'exit' to stop): ").strip()
        if item_name.lower() == "exit":
            break

        if item_name not in df["name"].values:
            print("Item not found!")
            continue

        quantity = float(input("Enter quantity: "))
        product = df[df["name"] == item_name].iloc[
            0
        ]  # Stores the entire Row : [Rice  50  50 ]
        if quantity > product["quantity"]:
            print("Not enough stock!")
            continue

        price = product["price"] * quantity
        sales.append({"name": item_name, "quantity": quantity, "price": price})

    """ moresale=input("You want to add another product? Y/N")
        if moresale.upper()=="Y":
            continue"""

    return sales
