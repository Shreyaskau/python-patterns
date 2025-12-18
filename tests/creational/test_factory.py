import pytest

from patterns.creational.factory import (
    EnglishLocalizer,
    GreekLocalizer,
    get_localizer,
)


def test_english_localizer():
    localizer = EnglishLocalizer()
    assert localizer.localize("dog") == "dog"
    assert localizer.localize("cat") == "cat"
    assert localizer.localize("parrot") == "parrot"


def test_greek_localizer():
    localizer = GreekLocalizer()
    assert localizer.localize("dog") == "σκύλος"
    assert localizer.localize("cat") == "γάτα"
    assert localizer.localize("parrot") == "parrot"  # No translation available


def test_get_localizer_english():
    localizer = get_localizer("English")
    assert isinstance(localizer, EnglishLocalizer)
    assert localizer.localize("dog") == "dog"


def test_get_localizer_greek():
    localizer = get_localizer("Greek")
    assert isinstance(localizer, GreekLocalizer)
    assert localizer.localize("dog") == "σκύλος"


def test_get_localizer_default():
    localizer = get_localizer()
    assert isinstance(localizer, EnglishLocalizer)


def test_get_localizer_unknown_language():
    localizer = get_localizer("Unknown")
    assert isinstance(localizer, EnglishLocalizer)  # Defaults to English


def test_localizer_translations():
    english = get_localizer("English")
    greek = get_localizer("Greek")
    
    assert english.localize("dog") == "dog"
    assert greek.localize("dog") == "σκύλος"
    
    assert english.localize("cat") == "cat"
    assert greek.localize("cat") == "γάτα"
    
    # Both should return untranslated words as-is
    assert english.localize("bear") == "bear"
    assert greek.localize("bear") == "bear"

