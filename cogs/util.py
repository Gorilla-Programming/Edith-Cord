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

    @commands.command(name = 'introduction' , aliases=['parichay','intro'])
    async def introduction(self,ctx):
        await ctx.send("I am a Edith, I was created on 7th January by our team VAR, You can check out all my features on 'https://edith-official.herokuapp.com/'")

    @commands.command(name = 'hi' , aliases=['hello','greetings'])
    async def hi(self,ctx):
        await ctx.send("Hey! you Idiot I am not a Chat bot to entertain you, go find some other bot")


def setup(bot):
  bot.add_cog(util(bot))