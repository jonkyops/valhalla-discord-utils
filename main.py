import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!valhalla ')

group_roles = ['Tanks', 'DPS', 'Healers']
class_roles = ['Druids', 'Hunters', 'Mages', 'Paladins',
               'Priests', 'Rogues', 'Warlocks', 'Warriors']
profession_roles = ['Alchemists', 'Blacksmiths', 'Enchanters', 'Engineers',
                    'Herbalists', 'Leatherworkers', 'Miners', 'Skinners', 'Tailors']

# region utils


def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
    if len(a_set.intersection(b_set)) > 0:
        return(True)
    return(False)
# endregion utils


@commands.has_role('Officers')
@bot.command(name='list-missing-roles', help='lists users that are missing required roles from the guild-roles channel')
async def list_users_missing_roles(ctx):
    members = filter(lambda x: x.bot == False, ctx.guild.members)
    results = []
    for member in members:

        # build up the list of roles the user has
        roles = [role.name for role in member.roles]

        # see if the roles the user has matches anything in the required lists
        group_assigned = common_member(roles, group_roles)
        class_assigned = common_member(roles, class_roles)
        professions_assigned = common_member(roles, profession_roles)

        # any role types missing?
        if not all([group_assigned, class_assigned, professions_assigned]):

            # build up a string to print everything missing from the user
            missing_roles = []
            if group_assigned == False:
                missing_roles.append('group')
            if class_assigned == False:
                missing_roles.append('class')
            if professions_assigned == False:
                missing_roles.append('professions')
            
            results.append(
                '{0} - {1}'.format(member.display_name, '/'.join(missing_roles))
            )
        pass
    
    if len(results) > 0:
        lines = '\n\t * '.join(results)
        await ctx.send(f'Guild Members Missing Roles:\n\t * {lines}')
    else:
        await ctx.send(f'No missing roles! ...What are you hiding?')
bot.run(TOKEN)
