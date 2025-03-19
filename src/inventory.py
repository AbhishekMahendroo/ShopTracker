import pandas as pd


def load_inventory(file_path: str) -> pd.DataFrame:
    """Loads inventory from an Excel file."""
    return pd.read_excel(file_path)


def save_inventory(df: pd.DataFrame, file_path: str) -> None:
    """Saves updated inventory to an Excel file."""
    df.to_excel(file_path, index=False)


def update_inventory(df: pd.DataFrame, sales: list) -> pd.DataFrame:
    """Updates the inventory after sales."""
    for sale in sales:
        df.loc[df["name"] == sale["name"], "quantity"] -= sale["quantity"]
    return df
