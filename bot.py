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
    if message.author == client.user:
        return


    if message.content.startswith('$hello'):
        await message.channel.send(f"Hello there {message.author.name}")


    if message.content.startswith('$numofusers'):
        await message.channel.send (f"```{server.member_count}```")


    if message.content.startswith('$dm'):
        await message.author.send (""""Hello I am the official AI Academy bot, Reginald!
    You might notice that the AI Academy discord is empty, but that's not the case. 
    First, let me ask you, what locationg are you from?
    1. Nautilus Middle 
    2. Kinloch Park Middle
    3. NMB Library""")


    if message.content.startswith('$roles'):
        await message.channel.send(f'your roles are {message.author.roles[1:]}')


    if message.content.startswith("$location 1"):
        if message.guild.roles[4] not in message.author.roles[1:]:
            await message.author.add_roles(message.guild.roles[1], reason="user responded with 1", atomic = True)
            await message.channel.send("I have added the appropriate tags to your user")
        if message.guild.roles[4] in message.author.roles[1:]:
            await message.channel.send("You already have that tag")

    if message.content.startswith("$location 2"):
        if message.guild.roles[2] not in message.author.roles[1:]:
            await message.author.add_roles(message.guild.roles[1], reason="user responded with 1", atomic = True)
            await message.channel.send("I have added the appropriate tags to your user")
        if message.guild.roles[2] in message.author.roles[1:]:
            await message.channel.send("You already have that tag")

    if message.content.startswith("$location 3"):
        if message.guild.roles[3] not in message.author.roles[1:]:
            await message.author.add_roles(message.guild.roles[1], reason="user responded with 1", atomic = True)
            await message.channel.send("I have added the appropriate tags to your user")
        if message.guild.roles[3] in message.author.roles[1:]:
            await message.channel.send("You already have that tag")


@client.event
async def on_member_join(member):
    await member.send("""Hello I am the official AI Academy bot, Reginald!
    You might notice that the AI Academy discord is empty, but that's not the case. 
    First, let me ask you, what locationg are you from?
    1. Nautilus Middle 
    2. Kinloch Park Middle
    3. NMB Library""")

client.run(token.read())