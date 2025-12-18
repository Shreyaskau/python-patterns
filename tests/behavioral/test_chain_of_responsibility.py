import pytest

from patterns.behavioral.chain_of_responsibility import (
    ConcreteHandler0,
    ConcreteHandler1,
    ConcreteHandler2,
    FallbackHandler,
    Handler,
)


def test_concrete_handler0_handles_range_0_to_9():
    handler = ConcreteHandler0()
    result = handler.check_range(5)
    assert result is True


def test_concrete_handler0_does_not_handle_out_of_range():
    handler = ConcreteHandler0()
    result = handler.check_range(15)
    assert result is None


def test_concrete_handler1_handles_range_10_to_19():
    handler = ConcreteHandler1()
    result = handler.check_range(15)
    assert result is True


def test_concrete_handler1_does_not_handle_out_of_range():
    handler = ConcreteHandler1()
    result = handler.check_range(5)
    assert result is None


def test_concrete_handler2_handles_range_20_to_29():
    handler = ConcreteHandler2()
    result = handler.check_range(25)
    assert result is True


def test_concrete_handler2_does_not_handle_out_of_range():
    handler = ConcreteHandler2()
    result = handler.check_range(15)
    assert result is None


def test_fallback_handler_always_returns_false():
    handler = FallbackHandler()
    result = handler.check_range(100)
    assert result is False


def test_handler_chain_processing():
    h0 = ConcreteHandler0()
    h1 = ConcreteHandler1()
    h2 = ConcreteHandler2(FallbackHandler())
    h0.successor = h1
    h1.successor = h2

    # Test that requests are handled by appropriate handlers
    # Request 5 should be handled by h0
    h0.handle(5)
    # Request 15 should be handled by h1
    h0.handle(15)
    # Request 25 should be handled by h2
    h0.handle(25)
    # Request 35 should fall through to FallbackHandler
    h0.handle(35)


def test_handler_without_successor():
    handler = ConcreteHandler0()
    # Should not raise an error when no successor
    handler.handle(5)


def test_handler_abstract_method():
    with pytest.raises(TypeError):
        Handler()  # Cannot instantiate abstract class

