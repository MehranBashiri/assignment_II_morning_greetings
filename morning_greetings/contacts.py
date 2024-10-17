class Friend:
    def __init__(self, name: str, contact_info: str, greeting_time: str):
        self.name = name
        self.contact_info = contact_info
        self.greeting_time = greeting_time


class ContactManager:
    def __init__(self):
        self.friends = []

    def add_friend(self, name: str, contact_info: str, greeting_time: str):
        
        if not name or not contact_info or not greeting_time:
            print("Error: Name, contact information, and greeting time are required.")
            return

        if any(friend.name == name for friend in self.friends):
            print(f"Friend with name {name} already exists.")
            return

        friend = Friend(name, contact_info, greeting_time)
        self.friends.append(friend)
        print(f"Added friend: {name}")

    def remove_friend(self, name: str):
        if not self.friends:
            print("Error: No friends in the list to remove.")
            return

        original_count = len(self.friends)
        self.friends = [friend for friend in self.friends if friend.name != name]

        if len(self.friends) < original_count:
            print(f"Removed friend: {name}")
        else:
            print(f"Error: Friend with name {name} not found.")

    def update_friend(self, name: str, contact_info: str = None, greeting_time: str = None):
        if not self.friends:
            print("Error: No friends in the list to update.")
            return

        for friend in self.friends:
            if friend.name == name:
                if contact_info:
                    friend.contact_info = contact_info
                if greeting_time:
                    friend.greeting_time = greeting_time
                print(f"Updated friend: {name}")
                return

        print(f"Error: Friend with name {name} not found.")

    def list_friends(self):
        if not self.friends:
            print("Error: No friends in the list.")
        else:
            for friend in self.friends:
                print(f"Name: {friend.name}, Contact: {friend.contact_info}, Greeting Time: {friend.greeting_time}")
        return self.friends



