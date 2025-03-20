import pandas as pd


class InventoryManager:
    """Class to manage inventory operations."""

    def __init__(self, file_path: str):
        """
        Initializes the InventoryManager with the file path.
        
        Args:
            file_path (str): Path to the inventory Excel file.
        """
        self.file_path = file_path
        self.inventory = self.load_inventory()

    def load_inventory(self) -> pd.DataFrame:
        """Loads inventory from an Excel file."""
        return pd.read_excel(self.file_path)

    def save_inventory(self) -> None:
        """Saves updated inventory to the Excel file."""
        self.inventory.to_excel(self.file_path, index=False)

    def update_inventory(self, sales: list) -> None:
        """
        Updates the inventory after sales.

        Args:
            sales (list): List of sales, where each sale is a dictionary
                          containing 'name' and 'quantity'.
        """
        for sale in sales:
            self.inventory.loc[self.inventory["name"] == sale["name"], "quantity"] -= sale["quantity"]
