from morning_greetings import ContactManager, send_message

def main():
    contact_manager = ContactManager()
    contact_manager.add_friend("Sara", "sara2018@gmail.com", "8:00 AM")
    contact_manager.add_friend("Ali", "ali32@gmail.com", "8:30 AM")
    contact_manager.add_friend("Nina", "nina2008@gmail.com", "8:30 AM")

    print("\nContacts added successfully!\n")

    friends_list = contact_manager.list_friends()
    if not friends_list:
        print("No friends in the list to send messages.")
        return

    print("Starting to send messages...\n")
    for friend in friends_list:
        send_message(friend)

    print("\nAll messages have been sent successfully!\n")

if __name__ == '__main__':
    main()




