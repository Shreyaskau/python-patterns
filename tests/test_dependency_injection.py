import pytest

from patterns.dependency_injection import (
    ConstructorInjection,
    ParameterInjection,
    SetterInjection,
    midnight_time_provider,
    production_code_time_provider,
)


def test_midnight_time_provider():
    result = midnight_time_provider()
    assert result == "24:01"


def test_production_code_time_provider():
    result = production_code_time_provider()
    assert isinstance(result, str)
    assert ":" in result


def test_constructor_injection():
    time_with_ci = ConstructorInjection(midnight_time_provider)
    result = time_with_ci.get_current_time_as_html_fragment()
    assert result == '<span class="tinyBoldText">24:01</span>'


def test_constructor_injection_with_production():
    time_with_ci = ConstructorInjection(production_code_time_provider)
    result = time_with_ci.get_current_time_as_html_fragment()
    assert isinstance(result, str)
    assert "tinyBoldText" in result


def test_parameter_injection():
    time_with_pi = ParameterInjection()
    result = time_with_pi.get_current_time_as_html_fragment(midnight_time_provider)
    assert result == '<span class="tinyBoldText">24:01</span>'


def test_parameter_injection_with_production():
    time_with_pi = ParameterInjection()
    result = time_with_pi.get_current_time_as_html_fragment(production_code_time_provider)
    assert isinstance(result, str)
    assert "tinyBoldText" in result


def test_setter_injection():
    time_with_si = SetterInjection()
    time_with_si.set_time_provider(midnight_time_provider)
    result = time_with_si.get_current_time_as_html_fragment()
    assert result == '<span class="tinyBoldText">24:01</span>'


def test_setter_injection_without_setting():
    time_with_si = SetterInjection()
    with pytest.raises(AttributeError):
        time_with_si.get_current_time_as_html_fragment()


def test_setter_injection_with_production():
    time_with_si = SetterInjection()
    time_with_si.set_time_provider(production_code_time_provider)
    result = time_with_si.get_current_time_as_html_fragment()
    assert isinstance(result, str)
    assert "tinyBoldText" in result


def test_dependency_injection_flexibility():
    # Test that we can swap implementations easily
    ci1 = ConstructorInjection(midnight_time_provider)
    ci2 = ConstructorInjection(production_code_time_provider)
    
    result1 = ci1.get_current_time_as_html_fragment()
    result2 = ci2.get_current_time_as_html_fragment()
    
    assert result1 == '<span class="tinyBoldText">24:01</span>'
    assert result2 != result1  # Production time will be different

