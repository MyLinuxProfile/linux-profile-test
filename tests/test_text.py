from linuxp.utils.text import (
    text_question,
    text_command,
    text_info,
    text_error,
    table_options
)


def test_text_question():
    text_question(value="test_text_question")


def test_text_command():
    text_command(value="text_command", desc="Test")


def test_text_info():
    text_info(value="text_info", desc="Test")


def test_text_error():
    text_error(value="text_error")


def test_table_options():
    test_lit = [1, 'A', 'B', 'C']
    table_options(
        question="Test?",
        first_column="Description",
        options=test_lit
    )
