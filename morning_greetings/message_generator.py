import random
import datetime

def generate_message(friend):
    name = friend.name
    current_day = datetime.datetime.now().strftime('%A')
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')

    day_based_messages = {
        "Monday": f"Good Morning, {name}! Let's start the week strong on this fine {current_day}, {current_date}!",
        "Friday": f"Hey {name}, it's {current_day}, {current_date}! Wishing you a great end to the week!",
        "Saturday": f"Good Morning, {name}! Enjoy your relaxing {current_day}, {current_date}!",
        "Sunday": f"Good Morning, {name}! Have a peaceful {current_day}, {current_date}!",
        "default": [
            f"Good Morning, {name}! Hope you have a fantastic {current_day}, {current_date} ahead!",
            f"Hey {name}, wishing you a bright and wonderful {current_day}, {current_date} morning!",
            f"Morning {name}! May your {current_day}, {current_date} be filled with joy and success.",
            f"Hello {name}, rise and shine! Here's to a great {current_day}, {current_date} ahead."
        ]
    }
    if current_day in day_based_messages:
        if isinstance(day_based_messages[current_day], str):
            message = day_based_messages[current_day]
        else:
            message = random.choice(day_based_messages['default'])
    else:
        message = random.choice(day_based_messages['default'])

    return message





