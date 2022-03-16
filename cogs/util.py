from discord.ext import commands

class util(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    #Purge Command
    @commands.command(name = 'purge' , aliases=['clear','delete','clean'])
    @commands.has_permissions(administrator=True)
    async def purge(self,ctx, amount : int):
        if amount > 100:
            amount = 100
        await ctx.channel.purge(limit= amount + 1) 


def setup(bot):
  bot.add_cog(util(bot))