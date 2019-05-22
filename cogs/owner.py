import discord
from discord.ext import commands

import logging

class owner(commands.Cog):

    
    def __init__(self, bot):
        self.bot = bot

'''
    Insert your UserID here for a restart command. Note this works when the bot starts up as a SystemD process with Restart=Always enabled
    @commands.command()
    async def reload(self, ctx):
        if ctx.message.author.id != 175665880582062081:
            return
        else:
            await ctx.send("Restarting!")
            return await self.bot.logout()
'''
def setup(bot):
    bot.add_cog(owner(bot))
    print("Cog Loaded with no errors!")
