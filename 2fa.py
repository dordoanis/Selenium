from imessage_reader import fetch_data


def mfa():

    # Create a FetchData instance
    fd = fetch_data.FetchData()

    # Store messages in my_data
    # This is a list of tuples containing user id, message, date and service.
    # service -> iMessage or SMS
    my_data = fd.get_messages()

    # Saving the exec number, word (password) from messages.
    # The  [ -1 ] will give us the lest modify message.
    # The [ 1 ] will give us the  message as a list.
    # The [ 20:27 ] will present us the spot we nees at the message.

    tinder_mfa = (int(my_data[-1][1][20:27]))
    return tinder_mfa


# mfa()
