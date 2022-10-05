import discord
class Archive():
    
    def __init__(self, client: discord.Bot, channel: discord.channel.Channel) -> None:
        self.client = client
        self.channel = channel

    