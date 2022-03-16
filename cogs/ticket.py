import discord
from discord.ext import commands
import json
from discord.ui import Button, View
from random import randint



class ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def createticket(self, ctx, *args):
        await ctx.channel.purge(limit=1)
        format_args = list(args)

        guild_id = ctx.message.guild.id
        channel_id = int(format_args[0].strip('<').strip('>').replace('#', ''))
        title = ' '.join(format_args[1:])

        with open('ticket.json', 'r') as file:
            ticket_data = json.load(file)
            new_ticket = str(guild_id)

            # Update existing ticket
            if new_ticket in ticket_data:
                ticket_data[new_ticket] += [channel_id]
                with open('ticket.json', 'w') as update_ticket_data:
                    json.dump(ticket_data, update_ticket_data, indent=4)

            # Add new ticket
            else:
                ticket_data[new_ticket] = [channel_id]
                with open('ticket.json', 'w') as new_ticket_data:
                    json.dump(ticket_data, new_ticket_data, indent=4)

        # Create new embed with reaction
        button = Button(label="Raise Ticket", style=discord.ButtonStyle.danger)
        view = View()
        view.add_item(button)
        ticket_embed = discord.Embed(colour=randint(0, 0xffffff))
        ticket_embed.set_thumbnail(
            url=f'https://cdn.discordapp.com/icons/{guild_id}/{ctx.message.guild.icon}.png')

        ticket_embed.add_field(name=f'Welcome To {ctx.message.guild} Server', value=f'{title}')
        send_ticket_embed = await self.bot.get_channel(channel_id).send(embed=ticket_embed, view = view)

        async def button_callback(interaction):
            if interaction.user.id != self.bot.user.id:
                with open('ticket.json', 'r') as file:
                    ticket_data = json.load(file)
                    
                channel_id = list(ticket_data.values())
                
                user_channel_id = interaction.channel_id
                
                for items in channel_id:
                    if user_channel_id in items:
                        # Get guild and roles
                        find_guild = discord.utils.find(lambda guild: guild.id == interaction.guild_id, self.bot.guilds)
                        guild_roles = discord.utils.get(find_guild.roles, name=f'{interaction.user.name}')

                        if guild_roles is None:
                            # Create new role
                            permissions = discord.Permissions(send_messages=True, read_messages=True)
                            await find_guild.create_role(name=f'{interaction.user.name}', permissions=permissions)
                            
                            # Assign new role
                            new_user_role = discord.utils.get(find_guild.roles, name=f'{interaction.user.name}')
                            await interaction.user.add_roles(new_user_role, reason=None, atomic=True)
                            
                            # Overwrite role permissions
                            admin_role = discord.utils.get(find_guild.roles, name='Admin')
                            

                            overwrites = {
                                find_guild.default_role: discord.PermissionOverwrite(read_messages=False),
                                new_user_role: discord.PermissionOverwrite(read_messages=True),
                                admin_role: discord.PermissionOverwrite(read_messages=True)
                            }
                            # Create new channel
                            create_channel = await find_guild.create_text_channel(
                                u'\U0001F4CB-{}'.format(new_user_role), overwrites=overwrites)
                            
                            buttonclose = Button(label="Close Ticket", style=discord.ButtonStyle.danger)
                            viewclose = View()
                            viewclose.add_item(buttonclose)

                            await create_channel.send(
                                f'{new_user_role.mention} Your ticket has been created! Please wait for '
                                f'{admin_role.mention} to response.', view = viewclose)                   

        button.callback =  button_callback

        #await send_ticket_embed.add_reaction(u'\U0001F3AB')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def closeticket(self, ctx, mentioned_user):
        mentioned_role = mentioned_user.strip('<@&>')
        get_mentioned_role = [items.name for items in ctx.message.author.guild.roles if f'{items.id}' in
                              f'{mentioned_role}']
        print(get_mentioned_role)
        get_role = discord.utils.get(ctx.message.author.guild.roles, name=f'{get_mentioned_role[0]}')
        #print(get_role)

        await get_role.delete(reason='Removed by command')
        await ctx.message.channel.delete(reason=None)
  
def setup(bot):
  bot.add_cog(ticket(bot))