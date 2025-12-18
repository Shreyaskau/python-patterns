import pytest

from patterns.structural.mvc import (
    ConsoleView,
    Controller,
    Model,
    ProductModel,
    Router,
    View,
)


def test_product_model_price():
    price = ProductModel.Price(1.50)
    assert float(price) == 1.50
    assert str(price) == "1.50"


def test_product_model_initialization():
    model = ProductModel()
    assert model.item_type == "product"


def test_product_model_iteration():
    model = ProductModel()
    products = list(model)
    assert "milk" in products
    assert "eggs" in products
    assert "cheese" in products


def test_product_model_get():
    model = ProductModel()
    milk_info = model.get("milk")
    assert milk_info["price"] == ProductModel.Price(1.50)
    assert milk_info["quantity"] == 10


def test_product_model_get_nonexistent():
    model = ProductModel()
    with pytest.raises(KeyError):
        model.get("nonexistent")


def test_console_view_initialization():
    view = ConsoleView()
    assert isinstance(view, View)


def test_console_view_capitalizer():
    assert ConsoleView.capitalizer("hello") == "Hello"
    assert ConsoleView.capitalizer("WORLD") == "World"


def test_console_view_show_item_list():
    view = ConsoleView()
    # Should not raise errors
    view.show_item_list("product", ["milk", "eggs"])


def test_console_view_show_item_information():
    view = ConsoleView()
    item_info = {"price": ProductModel.Price(1.50), "quantity": 10}
    # Should not raise errors
    view.show_item_information("product", "milk", item_info)


def test_console_view_item_not_found():
    view = ConsoleView()
    # Should not raise errors
    view.item_not_found("product", "nonexistent")


def test_controller_initialization():
    model = ProductModel()
    view = ConsoleView()
    controller = Controller(model, view)
    assert controller.model == model
    assert controller.view == view


def test_controller_show_items():
    model = ProductModel()
    view = ConsoleView()
    controller = Controller(model, view)
    # Should not raise errors
    controller.show_items()


def test_controller_show_item_information():
    model = ProductModel()
    view = ConsoleView()
    controller = Controller(model, view)
    # Should not raise errors
    controller.show_item_information("milk")
    controller.show_item_information("eggs")
    controller.show_item_information("cheese")


def test_controller_show_item_information_nonexistent():
    model = ProductModel()
    view = ConsoleView()
    controller = Controller(model, view)
    # Should not raise errors
    controller.show_item_information("nonexistent")


def test_router_initialization():
    router = Router()
    assert router.routes == {}


def test_router_register():
    router = Router()
    router.register("products", Controller, ProductModel, ConsoleView)
    assert "products" in router.routes
    assert isinstance(router.routes["products"], Controller)


def test_router_resolve():
    router = Router()
    router.register("products", Controller, ProductModel, ConsoleView)
    controller = router.resolve("products")
    assert isinstance(controller, Controller)


def test_router_resolve_nonexistent():
    router = Router()
    with pytest.raises(KeyError):
        router.resolve("nonexistent")


def test_model_abstract():
    with pytest.raises(TypeError):
        Model()  # Cannot instantiate abstract class


def test_view_abstract():
    with pytest.raises(TypeError):
        View()  # Cannot instantiate abstract class

