from .message_generator import generate_message
from .logger import log_message
import re  
from datetime import datetime

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

def send_message(friend):
    try:
        if not is_valid_email(friend.contact_info):
            raise ValueError(f"Invalid email address for {friend.name}: {friend.contact_info}")
        
        message = generate_message(friend)
        if message is None:
            raise ValueError("Message generation failed.")
        
        print(f"{datetime.now()}: Sending message to {friend.name} at {friend.contact_info}:")
        print(message)
        print("Message sent successfully!\n")
        
        log_message(friend, message)
        return {
            "status": "success",
            "message": message,
            "email": friend.contact_info
        }  

    except ValueError as ve:
        print(f"Validation Error: {ve}")
    except Exception as e:
        print(f"Failed to send message to {friend.name}: {e}")
    return None  



