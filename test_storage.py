import json,pytest
from storage import load_history, save_history

def test_save_and_load_history(tmp_path):
    filename = tmp_path / "messages.json"

    original = [
        {
            "sender": "Alice",
            "text": "Hello",
            "category": "Normal",
            "muted": False
        }
    ]

    save_history(original, filename)

    loaded = load_history(filename)

    assert loaded == original


def test_load_missing_file(tmp_path):
    filename = tmp_path / "missing.json"
    assert load_history(filename) == []

def test_history_preserved(tmp_path):
    filename = tmp_path / "messages.json"
    initial_records = [
        {"sender": "Alice", "text": "Hello", "category": "Normal", "muted": False}
    ]
    save_history(initial_records, filename)
    new_record = {"sender": "Bob", "text": "Hi there", "category": "Normal", "muted": False}
    initial_records.append(new_record)
    save_history(initial_records, filename)
    loaded = load_history(filename)
    assert loaded == initial_records

def test_invalid_json(tmp_path):
    filename = tmp_path / "invalid.json"
    filename.write_text("{ invalid json", encoding="utf-8")

    with pytest.raises(json.JSONDecodeError):
        load_history(filename)
