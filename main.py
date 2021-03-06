import asyncio
import datetime
import json
import logging
from pathlib import Path
import aiohttp
import discord
from discord.ext import commands

client = discord.client

def config_load():
    with open('data/config.json', 'r', encoding='utf-8') as doc:
        return json.load(doc)


async def run():
    config = config_load()
    bot = Bot(config=config,
              description=config['description'])
    try:
        await bot.start(config['token'])
    except KeyboardInterrupt:
        await bot.logout()


class Bot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(
            command_prefix=self.get_prefix_,
            description=kwargs.pop('description')
        )
        self.session = aiohttp.ClientSession(loop=self.loop)
        self.start_time = None
        self.app_info = None

        self.loop.create_task(self.track_start())
        self.loop.create_task(self.load_all_extensions())
        

        await self.wait_until_ready()
        self.start_time = datetime.datetime.utcnow()


    async def get_prefix_(self, bot, message):
        prefix = ['!']
        return commands.when_mentioned_or(*prefix)(bot, message)


    async def load_all_extensions(self):
        await self.wait_until_ready()
        await asyncio.sleep(1) 
        cogs = [x.stem for x in Path('cogs').glob('*.py')]
        for extension in cogs:
            try:
                self.load_extension(f'cogs.{extension}')
                print(f'loaded {extension}')
            except Exception as e:
                error = f'{extension}\n {type(e).__name__} : {e}'
                print(f'failed to load extension {error}')
            print('-' * 10)


    async def on_ready(self):
        print('-' * 10)
        self.app_info = await self.application_info()
        await self.change_presence(activity=discord.Game('Pika Pika'))
        print(f'Logged in as: {self.user.name}\n'
              f'Using discord.py version: {discord.__version__}\n'
              f'Owner: {self.app_info.owner}\n')
        print('-' * 10)    


    async def on_message(self, message):
        if message.author.bot:
            return
        print(message)
        print(message.content)
        await self.process_commands(message)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
