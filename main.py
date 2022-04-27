import discord
import os
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='!', intents = intents)


client.lavalink_nodes = [
    {"host": "losingtime.dpaste.org", "port": 2124, "password": "SleepingOnTrains"},
    {"host": "lava.link", "port": 80, "password": "dismusic"}
]

client.load_extension('cogs.tictactoe')
client.load_extension('cogs.eventListener')
client.load_extension('cogs.util')
client.load_extension('cogs.poll')
client.load_extension('cogs.ticket')
client.load_extension('cogs.badwords')
client.load_extension('dismusic')

client.run(os.environ['TOKEN'])
