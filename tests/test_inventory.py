import os
import json
import pytest
from src.inventory import load_inventory, save_inventory, update_inventory

# Constant for file path
MOCK_INVENTORY_PATH = "tests/mock_inventory.json"

def test_load_inventory():
    """
    Test if load_inventory loads the data correctly.
    It checks if the loaded data is a list and is not empty.
    """
    data = load_inventory(MOCK_INVENTORY_PATH)
    assert isinstance(data, list), "Loaded data should be a list"
    assert len(data) > 0, "Inventory should not be empty"

def test_save_inventory():
    """
    Test if save_inventory saves the data correctly.
    It checks if the function returns True upon successful save.
    """
    result = save_inventory(
        MOCK_INVENTORY_PATH,
        [
            {"item": "apple", "quantity": 10, "price": 1.0},
            {"item": "banana", "quantity": 5, "price": 0.5},
        ],
    )
    assert result is True, "Failed to save inventory"

def test_update_inventory():
    """
    Test if update_inventory updates inventory data correctly.
    It checks if the inventory is updated as expected.
    """
    updated_data = {"item": "apple", "quantity": 20, "price": 1.2}
    result = update_inventory(MOCK_INVENTORY_PATH, updated_data)
    assert result is True, "Failed to update inventory"

    # Check if the update is reflected in the loaded inventory
    inventory = load_inventory(MOCK_INVENTORY_PATH)
    assert any(
        item["item"] == "apple" and item["quantity"] == 20 for item in inventory
    ), "Item was not updated correctly"

def create_mock_inventory():
    """
    Helper function to create a mock inventory file for testing purposes.
    This file will be used for the load and save inventory tests.
    """
    inventory_data = [
        {"item": "apple", "quantity": 10, "price": 1.0},
        {"item": "banana", "quantity": 5, "price": 0.5},
    ]
    with open(MOCK_INVENTORY_PATH, "w", encoding="utf-8") as file:
        json.dump(inventory_data, file, indent=4)

@pytest.fixture
def mock_inventory():
    """
    Fixture to set up and tear down mock inventory for tests.
    This will create and delete the mock inventory file.
    """
    create_mock_inventory()
    yield
    if os.path.exists(MOCK_INVENTORY_PATH):
        os.remove(MOCK_INVENTORY_PATH)
