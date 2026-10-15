def categorize_message(sender, message, is_muted):
    is_admin = sender == "Admin"
    is_urgent = "urgent" in message

    if is_muted:
        category = "Hidden"
    elif is_admin or is_urgent:
        category = "Priority"
    else:
        category = "Normal"

    return category


def create_message_record(sender, message, is_muted):
    category = categorize_message(sender, message, is_muted)

    return {
        "sender": sender,
        "text": message,
        "category": category,
        "muted": is_muted
    }

def parse_muted(value):
    text=value.strip().lower()
    if text == "yes":
        return True
    elif text == "no":
        return False
    else:
        raise ValueError("Invalid input for muted. Please enter 'yes' or 'no'.")