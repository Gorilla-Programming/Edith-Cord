import discord
from discord.ext import commands
import datetime

class eventListener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is ready")  

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        em = discord.Embed(color=0x12d600, description=f"Thank you {member.mention}, you're the member number {len(list(member.guild.members))}!")
        em.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
        em.set_image(url=f"{member.avatar_url}")
        em.timestamp = datetime.datetime.utcnow()
        channel = self.bot.get_channel(940123097015681074)

        if not channel:
            return

        await channel.send(embed=em)

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        emLeft = discord.Embed(color=0x12d600, description=f"Recognised that a member called " + member.name + " left")
        emLeft.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
        emLeft.set_image(url=f"{member.avatar_url}")
        emLeft.timestamp = datetime.datetime.utcnow()
        channel = self.bot.get_channel(950991092835319878)

        if not channel:
            return

        await channel.send(embed=emLeft)

def setup(bot):
  bot.add_cog(eventListener(bot))