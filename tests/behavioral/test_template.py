from unittest.mock import patch

import pytest

from patterns.behavioral.template import (
    convert_to_text,
    get_csv,
    get_pdf,
    get_text,
    saver,
    template_function,
)


def test_get_text():
    assert get_text() == "plain-text"


def test_get_pdf():
    assert get_pdf() == "pdf"


def test_get_csv():
    assert get_csv() == "csv"


def test_convert_to_text():
    result = convert_to_text("pdf")
    assert result == "pdf as text"


def test_template_function_with_text_and_save():
    with patch("patterns.behavioral.template.saver") as mock_saver:
        template_function(get_text, to_save=True)
        mock_saver.assert_called_once()


def test_template_function_with_pdf_and_converter():
    result = template_function(get_pdf, converter=convert_to_text)
    # Should convert pdf to text
    assert result is None  # Function returns None


def test_template_function_with_csv_and_save():
    with patch("patterns.behavioral.template.saver") as mock_saver:
        template_function(get_csv, to_save=True)
        mock_saver.assert_called_once()


def test_template_function_without_converter():
    # Should skip conversion for plain-text (length > 3)
    with patch("patterns.behavioral.template.saver") as mock_saver:
        template_function(get_text, converter=convert_to_text, to_save=False)
        mock_saver.assert_not_called()


def test_template_function_with_converter_for_short_data():
    # pdf has length <= 3, so should convert
    with patch("patterns.behavioral.template.convert_to_text") as mock_convert:
        mock_convert.return_value = "converted"
        template_function(get_pdf, converter=convert_to_text, to_save=False)
        mock_convert.assert_called_once()


def test_template_function_without_save():
    with patch("patterns.behavioral.template.saver") as mock_saver:
        template_function(get_text, to_save=False)
        mock_saver.assert_not_called()

