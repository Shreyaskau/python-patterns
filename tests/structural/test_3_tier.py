import importlib
import pytest

# Import module with numeric prefix using importlib
three_tier = importlib.import_module("patterns.structural.3-tier")
BusinessLogic = three_tier.BusinessLogic
Data = three_tier.Data
Ui = three_tier.Ui


def test_data_products():
    data = Data()
    result = data.__get__(None, None)
    assert "products" in result
    assert "milk" in result["products"]
    assert "eggs" in result["products"]
    assert "cheese" in result["products"]


def test_business_logic_product_list():
    business_logic = BusinessLogic()
    products = business_logic.product_list()
    assert "milk" in products
    assert "eggs" in products
    assert "cheese" in products


def test_business_logic_product_information():
    business_logic = BusinessLogic()
    milk_info = business_logic.product_information("milk")
    assert milk_info is not None
    assert milk_info["price"] == 1.50
    assert milk_info["quantity"] == 10


def test_business_logic_product_not_found():
    business_logic = BusinessLogic()
    result = business_logic.product_information("nonexistent")
    assert result is None


def test_ui_initialization():
    ui = Ui()
    assert isinstance(ui.business_logic, BusinessLogic)


def test_ui_get_product_list():
    ui = Ui()
    # Should not raise errors
    ui.get_product_list()


def test_ui_get_product_information():
    ui = Ui()
    # Should not raise errors
    ui.get_product_information("milk")
    ui.get_product_information("eggs")
    ui.get_product_information("cheese")


def test_ui_get_product_information_nonexistent():
    ui = Ui()
    # Should not raise errors
    ui.get_product_information("nonexistent")


def test_three_tier_separation():
    # Test that layers are properly separated
    ui = Ui()
    business_logic = ui.business_logic
    
    # UI should use business logic, not data directly
    assert hasattr(business_logic, "product_list")
    assert hasattr(business_logic, "product_information")
    
    # Business logic should have data
    assert hasattr(business_logic, "data")

