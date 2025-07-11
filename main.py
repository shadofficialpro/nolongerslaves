import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Load .env into environment
load_dotenv()

# Fetch from DISCORD_TOKEN env var
TOKEN = os.getenv('DISCORD_TOKEN')
if TOKEN is None:
    raise RuntimeError("DISCORD_TOKEN not set in environment")

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send("Pong! 🏓")

if __name__ == "__main__":
    bot.run(TOKEN)

