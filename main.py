import discord
import os

client = discord.Client()
token = os.environ['DISCORD_TOKEN']

group_roles = ['Tanks','DPS','Healers']
class_roles = ['Druids','Hunters','Mages','Paladins','Priests','Rogues','Warlocks','Warriors']
profession_roles = ['Alchemists','Blacksmiths','Enchanters','Engineers','Herbalists','Leatherworkers','Miners','Skinners','Tailors']

#region utils
def common_member(a, b): 
    a_set = set(a) 
    b_set = set(b) 
    if len(a_set.intersection(b_set)) > 0: 
        return(True)
    return(False)
#endregion utils

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ListUsersMissingRoles'):
        await list_users_missing_roles(message)

# ListUsersMissingRoles 
async def list_users_missing_roles(message):
    members = filter(lambda x: x.bot == False, message.channel.members)
    for member in members:

        # build up the list of roles the user has
        roles = []
        for role in member.roles:
            roles.append(role.name)

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
            
            await message.channel.send('{0} is missing {1}'.format(member.display_name,'/'.join(missing_roles)))
        pass

client.run(token)
