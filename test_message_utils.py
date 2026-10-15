import pytest
from message_utils import categorize_message, create_message_record, parse_muted

def test_admin_message():
    result = categorize_message("Admin", "Hello", False)
    assert result == "Priority"

def test_muted_admin():
    result = categorize_message("Admin", "urgent update", True)
    assert result == "Hidden"

def test_urgent_message():
    result = categorize_message("Bob", "urgent help", False)
    assert result == "Priority"

def test_normal_message():
    result = categorize_message("Alice", "Hello", False)
    assert result == "Normal"

def test_muted_urgent_message():
    result = categorize_message("Bob", "urgent help", True)
    assert result == "Hidden"

def test_message_record():
    record = create_message_record("Alice", "Hello", False)
    assert record == {
        "sender": "Alice",
        "text": "Hello",
        "category": "Normal",
        "muted": False
    }

def test_muted_yes():
    ismuted = parse_muted("yes")
    assert ismuted == True

def test_muted_case_insensitive():
    assert parse_muted("  No ") is False

def test_muted_invalid():
    with pytest.raises(ValueError):
        parse_muted("maybe")

def test_muted_empty():
    with pytest.raises(ValueError):
        parse_muted("")