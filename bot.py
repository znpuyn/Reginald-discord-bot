import discord 
from discord.utils import get
from discord.ext import commands

token = "NzE1MDczOTc2NDgwNjk0Mjc1.Xs36ww.gIKH3Lwspm2Hl4tWExKYBu-LQ8c"
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
        await message.author.send ("hi there 👀")
    if message.content.startswith('$roles'):
        await message.channel.send(f'your roles are {message.author.roles([1:])

@client.event
async def on_member_join(member):
    await member.send("hello there")

client.run(token)