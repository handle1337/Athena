import os
import discord

discord_token = os.environ['discord_token']


class DiscordBot(discord.Client):
    async def on_ready(self):
        print("test")
