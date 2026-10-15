from message_utils import create_message_record, parse_muted
from storage import save_history, load_history

def get_muted_status():
    while True:
        try:
            muted = input("Muted (yes/no): ")
            is_muted = parse_muted(muted)
            return is_muted

        except ValueError as error:
            print(error)

def main():
    message_history = load_history("message_history.json")

    for i in range(3):
        print(f"--- Message {i + 1} ---")

        sender = input("Sender: ")
        message = input("Message: ")
        is_muted = get_muted_status()

        record = create_message_record(sender, message, is_muted)
        message_history.append(record)

    save_history(message_history, "message_history.json")

    print("\n===== MESSAGE HISTORY =====")

    for record in message_history:
        print(f"Sender: {record['sender']}")
        print(f"Text: {record['text']}")
        print(f"Category: {record['category']}")
        print(f"Muted: {record['muted']}")
        print()


if __name__ == "__main__":
    main()