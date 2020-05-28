import discord 
from discord.utils import get
from discord.ext import commands

token = open("key.txt", "r")
client = discord.Client()

@client.event
async def on_connect():
    print ('I have successfully logged in as {0.user}'.format(client))

@client.event 
async def on_disconnect():
    print ("I have lost connection, please troubleshoot")

@client.event
async def on_ready():
    server = client.get_guild (715077503948947500)
    print ('I have fully initialized as {0.user}'.format(client))
    print ('joined '+ str(server))

@client.event
async def on_message(message):
    server = client.get_guild (715077503948947500) #needs to be somewhere where the bot has already initialized if not it returns none. 
    member = server.get_member(message.author.id)
    member_roles = member.roles[1:]
    role_names = []
    for name in member_roles:
        role_names.append(name.name)
    
    server_role_names = []
    for name in server.roles[1:]:
        server_role_names.append(name.name)

    if message.author == client.user:
        return


    if message.content.startswith('$hello'):
        await message.channel.send(f"Hello there {message.author.name}")


    if message.content.startswith('$students'):
        x = message.guild.roles[1].members
        students = []
        for count in x:
            students.append(count.name)
        await message.channel.send(f" AI Academy currently has:```{len(students)}```")


    if message.content.startswith('$dm'):
        await message.author.send (""""Hello I am the official AI Academy bot, Reginald!
You might notice that the AI Academy discord is empty, but that's not the case. 
First, let me ask you, what locationg are you from?
1. Nautilus Middle 
2. Kinloch Park Middle
3. NMB Library""")


    if message.content.startswith('$roles'):
        await message.channel.send(f'your roles are:\n```{role_names}```')

    if message.content.startswith('$guildroles'):
        await message.channel.send(f'{server_role_names}')

#Location commands and responses_________________________________________________________________________________________________________________________________________________   

    if message.content.startswith('$locations'):
        await message.channel.send(
"""The following locations are available:
1. Kinloch Park Middle
2. Nautilus Middle
3. NMB Library""")
          
    if message.content.startswith("1."):
        if server.roles[1] not in member_roles and server.roles[2 or 3] not in member_roles:
            await member.add_roles(server.roles[1], reason="user responded that they attend Kinloch", atomic = True)
            await message.channel.send("I have added the appropriate tag to your user")
        if server.roles[1] in member_roles:
            await message.channel.send("You already have that tag")


    if message.content.startswith("2."):
        if server.roles[2] not in member_roles and server.roles[1 or 3] not in member_roles:
            await member.add_roles(server.roles[2], reason="user responded that they attend Nautilus", atomic = True)
            await message.channel.send("I have added the appropriate tag to your user")
        if server.roles[2] in member_roles:
            await message.channel.send("You already have that tag")

    if message.content.startswith("3."):
        if server.roles[3] not in member_roles and server.roles[1 or 2] not in member_roles:
            await member.add_roles(server.roles[3], reason="user responded that they attend NMB", atomic = True)
            await message.channel.send("I have added the appropriate tag to your user")
        if server.roles[3] in member_roles:
            await message.channel.send("You already have that tag")


#end of Location commands and replies_____________________________________________________________________________________________________________________________________________


@client.event
async def on_member_join(member):
    await member.send("""Hello I am the official AI Academy bot, Reginald!
    You might notice that the AI Academy discord is empty, but that's not the case. 
    First, let me ask you, what locationg are you from?
    1. Nautilus Middle 
    2. Kinloch Park Middle
    3. NMB Library""")

client.run(token.read())