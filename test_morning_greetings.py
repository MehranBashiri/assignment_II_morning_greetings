import unittest
from unittest.mock import patch, mock_open
from morning_greetings import ContactManager, generate_message, send_message, log_message

class TestContactManager(unittest.TestCase):
    def setUp(self):
        self.contact_manager = ContactManager()

    def test_add_friend(self):
        self.contact_manager.add_friend("Maryam", "maryam@yahoo.com", "9:00 AM")
        self.assertEqual(len(self.contact_manager.list_friends()), 1)
        self.assertEqual(self.contact_manager.list_friends()[0].name, "Maryam")

    def test_remove_friend(self):
        self.contact_manager.add_friend("Maryam", "maryam@yahoo.com", "9:00 AM")
        self.contact_manager.remove_friend("Maryam")
        self.assertEqual(len(self.contact_manager.list_friends()), 0)

    def test_update_friend(self):
        self.contact_manager.add_friend("Maryam", "maryam@yahoo.com", "9:00 AM")
        self.contact_manager.update_friend("Maryam", contact_info="maryam32@yahoo.com", greeting_time="10:00 AM")
        friend = self.contact_manager.list_friends()[0]
        self.assertEqual(friend.contact_info, "maryam32@yahoo.com")
        self.assertEqual(friend.greeting_time, "10:00 AM")

    def test_list_friends(self):
        self.contact_manager.add_friend("Maryam", "maryam@yahoo.com", "9:00 AM")
        friends = self.contact_manager.list_friends()
        self.assertEqual(len(friends), 1)
        self.assertEqual(friends[0].name, "Maryam")

class TestMessageGenerator(unittest.TestCase):
    def test_generate_message(self):
        friend = type("Friend", (object,), {"name": "Maryam"})  # Simulate Friend object
        message = generate_message(friend)
        self.assertIn("Maryam", message)  # Ensure the friend's name is in the message

class TestSendMessage(unittest.TestCase):
    @patch('builtins.print')  # Mock print to capture output
    def test_send_message_success(self, mock_print):
        friend = type("Friend", (object,), {"name": "Maryam", "contact_info": "maryam@yahoo.com", "greeting_time": "9:00 AM"})
        message = send_message(friend)
        self.assertIsNotNone(message)
        self.assertIn("Sending message", mock_print.call_args_list[0][0][0])  # Check if the "Sending message" message was printed

class TestLogger(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open)
    def test_log_message(self, mock_file):
        friend = type("Friend", (object,), {"name": "Maryam", "contact_info": "maryam@yahoo.com", "greeting_time": "9:00 AM"})
        message = "Good Morning, Maryam!"
        
        # Call the log_message function
        log_message(friend, message)
        
        # Check that write was called, ignoring the exact timestamp
        mock_file().write.assert_called_with(
            unittest.mock.ANY  # Ignore the exact content of the write call
        )
        
        # Instead, check parts of the log that you expect
        log_file_content = mock_file().write.call_args[0][0]
        self.assertIn("To: Maryam", log_file_content)
        self.assertIn("Contact: maryam@yahoo.com", log_file_content)
        self.assertIn("Message: Good Morning, Maryam!", log_file_content)

if __name__ == '__main__':
    unittest.main()




