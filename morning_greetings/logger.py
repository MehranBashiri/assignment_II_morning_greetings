import datetime

def log_message(friend, message, log_file_path="sent_messages.log"):
    try:
        with open(log_file_path, "a") as log_file:
            log_entry = (
                f"Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"To: {friend.name}, Contact: {friend.contact_info}, "
                f"Scheduled Time: {friend.greeting_time}\n"
                f"Message: {message}\n\n"
            )
            log_file.write(log_entry)
            print(f"Message logged for {friend.name}.")
    except Exception as e:
        print(f"Error logging message for {friend.name}: {e}")




        
