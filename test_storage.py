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
    alice = {
        "sender": "Alice",
        "text": "Hello",
        "category": "Normal",
        "muted": False
    }

    bob = {
        "sender": "Bob",
        "text": "Hi there",
        "category": "Normal",
        "muted": False
    }
    save_history([alice], filename)
    history = load_history(filename)
    history.append(bob)
    
    save_history(history, filename)
    result = load_history(filename)

    assert result == [alice, bob]
    assert len(result) == 2

def test_invalid_json(tmp_path):
    filename = tmp_path / "invalid.json"
    filename.write_text("{ invalid json", encoding="utf-8")

    with pytest.raises(json.JSONDecodeError):
        load_history(filename)
