import discord
from discord.ext import commands

import random

class poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.emoji = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3',
                      '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001F51F']
                          
    @commands.command(name = 'poll')
    async def poll(self,ctx, question, option1=None, option2=None,option3= None ,option4=None, option5=None,option6= None,option7= None):
      if option1==None:
        await ctx.channel.purge(limit=1)
        myEmbed = discord.Embed(title= "NEW POLL",description=f"\n{question}\n**✅ = Yes**\n**❎ = No**",color=0x2ecc71)
        message = await ctx.send(embed=myEmbed)
        await message.add_reaction('❎')
        await message.add_reaction('✅')
      elif option2==None:
        await ctx.channel.purge(limit=1)
        myEmbed = discord.Embed(title= "NEW POLL",description=f"\n{question}\n**{self.emoji[0]} = {option1}**",color=0x2ecc71)
        message = await ctx.send(embed=myEmbed)
        for i in range(1):
            await message.add_reaction(self.emoji[i])
      elif option3==None:
        await ctx.channel.purge(limit=1)
        myEmbed = discord.Embed(title= "NEW POLL",description=f"\n{question}\n**{self.emoji[0]} = {option1}**\n**{self.emoji[1]} = {option2}**",color=0x2ecc71)
        message = await ctx.send(embed=myEmbed)
        for i in range(2):
            await message.add_reaction(self.emoji[i])
      elif option4==None:
        await ctx.channel.purge(limit=1)
        myEmbed = discord.Embed(title= "NEW POLL",description=f"\n{question}\n**{self.emoji[0]} = {option1}**\n**{self.emoji[1]} = {option2}**\n**{self.emoji[2]} = {option3}**",color=0x2ecc71)
        message = await ctx.send(embed=myEmbed)
        for i in range(3):
            await message.add_reaction(self.emoji[i])
      elif option5==None:
        await ctx.channel.purge(limit=1)
        myEmbed = discord.Embed(title= "NEW POLL",description=f"\n{question}\n**{self.emoji[0]} = {option1}**\n**{self.emoji[1]} = {option2}**\n**{self.emoji[2]} = {option3}**\n**{self.emoji[3]} = {option4}**",color=0x2ecc71)
        message = await ctx.send(embed=myEmbed)
        for i in range(4):
            await message.add_reaction(self.emoji[i])
      elif option6==None:
        await ctx.channel.purge(limit=1)
        myEmbed = discord.Embed(title= "NEW POLL",description=f"\n{question}\n**{self.emoji[0]} = {option1}**\n**{self.emoji[1]} = {option2}**\n**{self.emoji[2]} = {option3}**\n**{self.emoji[3]} = {option4}**\n**{self.emoji[4]} = {option5}**",color=0x2ecc71)
        message = await ctx.send(embed=myEmbed)
        for i in range(5):
            await message.add_reaction(self.emoji[i])
      elif option7==None:
        await ctx.channel.purge(limit=1)
        myEmbed = discord.Embed(title= "NEW POLL",description=f"\n{question}\n**{self.emoji[0]} = {option1}**\n**{self.emoji[1]} = {option2}**\n**{self.emoji[2]} = {option3}**\n**{self.emoji[3]} = {option4}**\n**{self.emoji[4]} = {option5}**\n**{self.emoji[5]} = {option6}**",color=0x2ecc71)
        message = await ctx.send(embed=myEmbed)
        for i in range(6):
            await message.add_reaction(self.emoji[i])
      else:
        await ctx.channel.purge(limit=1)
        myEmbed = discord.Embed(title= "ERROR",description="Can not create poll for more than 6 options at this moment, please try again after some time",color=0x2ecc71)
        message = await ctx.send(embed=myEmbed)

          

  
def setup(bot):
  bot.add_cog(poll(bot))