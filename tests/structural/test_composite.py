import pytest

from patterns.structural.composite import CompositeGraphic, Ellipse, Graphic


def test_ellipse_initialization():
    ellipse = Ellipse("1")
    assert ellipse.name == "1"


def test_ellipse_render():
    ellipse = Ellipse("test")
    # Should not raise an error
    ellipse.render()


def test_composite_graphic_initialization():
    composite = CompositeGraphic()
    assert len(composite.graphics) == 0


def test_composite_graphic_add():
    composite = CompositeGraphic()
    ellipse = Ellipse("1")
    composite.add(ellipse)
    assert len(composite.graphics) == 1
    assert ellipse in composite.graphics


def test_composite_graphic_remove():
    composite = CompositeGraphic()
    ellipse = Ellipse("1")
    composite.add(ellipse)
    composite.remove(ellipse)
    assert len(composite.graphics) == 0


def test_composite_graphic_render():
    composite = CompositeGraphic()
    ellipse1 = Ellipse("1")
    ellipse2 = Ellipse("2")
    composite.add(ellipse1)
    composite.add(ellipse2)
    # Should not raise an error
    composite.render()


def test_nested_composite():
    ellipse1 = Ellipse("1")
    ellipse2 = Ellipse("2")
    
    graphic1 = CompositeGraphic()
    graphic1.add(ellipse1)
    graphic1.add(ellipse2)
    
    ellipse3 = Ellipse("3")
    graphic2 = CompositeGraphic()
    graphic2.add(ellipse3)
    
    main_graphic = CompositeGraphic()
    main_graphic.add(graphic1)
    main_graphic.add(graphic2)
    
    assert len(main_graphic.graphics) == 2
    assert len(graphic1.graphics) == 2
    assert len(graphic2.graphics) == 1


def test_graphic_abstract():
    with pytest.raises(TypeError):
        Graphic()  # Cannot instantiate abstract class


def test_composite_graphic_is_graphic():
    composite = CompositeGraphic()
    assert isinstance(composite, Graphic)


def test_ellipse_is_graphic():
    ellipse = Ellipse("test")
    assert isinstance(ellipse, Graphic)

