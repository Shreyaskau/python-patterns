import pytest

from patterns.behavioral.registry import (
    BaseRegisteredClass,
    RegistryHolder,
)


def test_base_registered_class_in_registry():
    assert "BaseRegisteredClass" in RegistryHolder.REGISTRY
    assert RegistryHolder.REGISTRY["BaseRegisteredClass"] == BaseRegisteredClass


def test_subclass_automatically_registered():
    class ClassRegistree(BaseRegisteredClass):
        def __init__(self, *args, **kwargs):
            pass

    assert "ClassRegistree" in RegistryHolder.REGISTRY
    assert RegistryHolder.REGISTRY["ClassRegistree"] == ClassRegistree


def test_multiple_subclasses_registered():
    class ClassA(BaseRegisteredClass):
        pass

    class ClassB(BaseRegisteredClass):
        pass

    assert "ClassA" in RegistryHolder.REGISTRY
    assert "ClassB" in RegistryHolder.REGISTRY
    assert RegistryHolder.REGISTRY["ClassA"] == ClassA
    assert RegistryHolder.REGISTRY["ClassB"] == ClassB


def test_get_registry():
    registry = RegistryHolder.get_registry()
    assert isinstance(registry, dict)
    assert "BaseRegisteredClass" in registry


def test_registry_contains_all_classes():
    class TestClass1(BaseRegisteredClass):
        pass

    class TestClass2(BaseRegisteredClass):
        pass

    registry = RegistryHolder.get_registry()
    assert "BaseRegisteredClass" in registry
    assert "TestClass1" in registry
    assert "TestClass2" in registry

