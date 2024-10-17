# Morning Greetings

## Overview
**Morning Greetings** is a Python package that automates the process of sending personalized "Good Morning" messages. It allows you to manage contacts, generate custom messages, simulate sending them, and log the message details for future reference.

## Requirements
- Python 3.6 or higher
- No external dependencies

## Package Structure
- `morning_greetings/contacts.py`: Manage the contact list (add, update, remove friends).
- `morning_greetings/message_generator.py`: Generate personalized "Good Morning" messages.
- `morning_greetings/message_sender.py`: Simulate sending messages.
- `morning_greetings/logger.py`: Log the details of each message sent.
- `test_morning_greetings.py`: Unit tests to verify functionality for contact management, message generation, sending, and logging.
- `main.py`: The main script that integrates all modules and executes the message-sending process.
- `sent_messages.log`: Log file that stores the history of sent messages.
- `setup.py`: The setup file for packaging and installation.

## Installation

To install this package, follow these steps:

1. Clone the project:
    git clone https://github.com/mehranbashiri/assignment_II_morning_greetings.git

2. Navigate to the project directory and install the package:
    cd assignment_02_morning_greetings
    pip install .

## Usage

1. After installation, navigate to the folder containing `main.py`.
2. Run the program using:
    python main.py

### Managing Contacts
Use the `ContactManager` class to manage your contacts:
- Add a friend
- Update a friend's contact info or greeting time
- Remove a friend

### Reviewing Logs
All sent messages are recorded in the `sent_messages.log` file. Each entry includes the recipient’s name, contact information, scheduled greeting time, and the message content.

## Running Unit Tests

To ensure all components are working as expected, run the unit tests:

1. Navigate to the project directory.
2. Execute the test suite with:
    python test_morning_greetings.py

The tests will verify the functionality of contact management, message generation, message sending, and logging.

## Author
- Mehran Bashiri
