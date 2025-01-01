import requests
class Ray:
    def __init__(self,token,guild_id):
        self.token = token
        self.guild_id = guild_id

    def __verify_token(self):
        """
        function to verify the token 
        """
        url = "https://discord.com/api/v10/users/@me"
        headers = {"Authorization": f"Bot {self.token}"}
        req = requests.get(url=url, headers=headers)

        if req.status_code == 200:
            print("Token is valid :0")
            return True
        else:
            print(f"Invalid token is invalid :0")
            return False

    def __verify_guild(self):
        """
        checks the guild id
        """

        if not self.__verify_token():
            return { "Invalid token. Cannot fetch guild data."}

        url = f"https://discord.com/api/v10/guilds/{self.guild_id}"
        headers = {"Authorization": f"Bot {self.token}"}
        req = requests.get(url=url, headers=headers)

        if req.status_code == 200:
            return True
        else:
            return "Invalid guild id :0 maybe the bot is not in the guild"

    
    def spam_channels(self,count:int,message:str):
        """
        spam all channels in a server
        """
        if not self.__verify_token() and not self.__verify_guild():
            return {"Invalid token  or guild id"}

        url = f"https://discord.com/api/v10/guilds/{self.guild_id}/channels"
        headers = {"Authorization": f"Bot {self.token}"}
        response = requests.get(url=url, headers=headers)

        if response.status_code != 200:
            return {"Failed to fetch channels.":response.json()}

        channels = response.json()

        results = {"success": [], "failed": []}

        for channel in channels:
            for _ in range(count):
                message_url = f"https://discord.com/api/v10/channels/{channel['id']}/messages"
                payload = {"content": message}
                msg_response = requests.post(url=message_url, headers=headers, json=payload)

                if msg_response.status_code == 200:
                    results["success"].append({"channel_id": channel["id"], "message_id": msg_response.json()["id"]})
                else:
                    results["failed"].append({"channel_id": channel["id"], "error": msg_response.json()})

        return results
