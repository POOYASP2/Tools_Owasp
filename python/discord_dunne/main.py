import os
import json
import asyncio
import datetime
import requests
from requests.exceptions import HTTPError
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
time = datetime.datetime.now
bot = commands.Bot(command_prefix='!')

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
DISCORD_TARGET_CHANNEL_ID = int(os.getenv("DISCORD_TARGET_CHANNEL_ID"))

DUNE_API = "https://the-dune-api.herokuapp.com"


def get_request(count):
    try:
        response = requests.get(f"{DUNE_API}/quotes/{count}")
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        return json.loads(response.text)


async def quote_generator():
    await bot.wait_until_ready()

    channel = bot.get_channel(DISCORD_TARGET_CHANNEL_ID)

    print(f'{time()} - Bot is ready.')
    count = input(f'{time()} - Enter number of quotes: ')

    for quote in get_request(count):
        await channel.send(quote['quote'])
        print(f'{time()} - Message sent.')
        await asyncio.sleep(1)

    print(f'{time()} - Bot is shutting down.')
    await bot.close()

bot.loop.create_task(quote_generator())
bot.run(DISCORD_BOT_TOKEN)
