import discord
from discord.ext import commands
import json
import aiohttp
import time
import asyncio
from datetime import datetime
from datetime import time
import logging
import random as rng

logger = logging.getLogger()
client = discord.client

class pika(commands.Cog):

    

    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def pikadoubt(self, ctx):
        await ctx.send('https://i.kym-cdn.com/photos/images/original/001/431/714/db0.jpg_large')

    @commands.command()
    async def pikasip(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/561720503522426900/580382970657898527/detective-pikachu-1169793-1280x0.jpeg')

    @commands.command()
    async def pikawhat(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/561720503522426900/580384729044484110/20190521_142120.jpg')

    @commands.command()
    async def pikawoah(self, ctx):
        await ctx.send('https://i.kym-cdn.com/photos/images/facebook/001/430/795/975.jpg')

    @commands.command()
    async def pikapride(self, ctx):
        await ctx.send('https://media.discordapp.net/attachments/520708656216539165/583251464944746496/pikapride.jpg')
    
    @commands.command()
    async def pikasad(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/520708656216539165/583251480363139072/pikasad.jpg')


    @commands.Cog.listener()
    async def on_message(self, message):
        pikapika = rng.choice(["pika pika", "pika?", "pika pika!", "pika!", "pikaaaachuuuuu", "Pi-Pikachu!", "Pika-Pikachu", "Pi-kaPika"])
        if message.author.bot:
            return
        if "!" in message.content:
            return
        if ":" in message.content:
            return
        if "pika" in message.content.lower():
            await message.channel.send(pikapika)


    @commands.command()
    async def ping(self, ctx):
        latency = self.bot.latency
        latencyfix = round(latency, 2)
        await ctx.send(latencyfix)
        

def setup(bot):
    bot.add_cog(pika(bot))
    print("Cog Loaded with no errors!")

