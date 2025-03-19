# ShopSalesTracker

ShopSalesTracker is a Python-based sales tracking system designed for small shops. It allows shop owners to manage inventory, process daily sales, generate invoices with GST, and maintain a record of daily transactions.

## Features
- **Inventory Management:** Load and update product stock from an Excel file.
- **Sales Processing:** Enter sales details, calculate totals with GST, and generate bills.
- **Daily Sales Log:** Maintain a record of daily transactions in an Excel file.
- **Automatic Stock Updates:** Deduct sold quantities from the inventory.
- **User-Friendly CLI Interface:** Simple command-line interface for ease of use.

## Project Structure
```
ShopSalesTracker/
│-- src/
│   │-- main.py          # Entry point of the application
│   │-- utils.py         # Helper functions (if needed)
│   │-- inventory.py     # Inventory management functions
│   │-- sales.py         # Sales processing and billing
│-- data/
│   │-- shop_inventory.xlsx  # Initial inventory data
│   │-- daily_sales.xlsx     # Sales logs
│-- README.md
│-- requirements.txt     # Required dependencies
│-- setup.py            # Package setup file
```

## Installation
Ensure you have Python 3.6+ installed. Then, run:
```bash
pip install -r requirements.txt
```

## Usage
Run the application using:
```bash
python src/main.py
```
Follow the on-screen instructions to make sales and generate daily reports.

## Contributing
Contributions are welcome! Fork the repository and submit a pull request with improvements.

## License
This project is licensed under the MIT License.
