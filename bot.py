import discord 
from discord.utils import get
from discord.ext import commands

token = open("key.txt", "r")
bot = commands.Bot(command_prefix='$')

@bot.command()
async def whatisserverrole (ctx, arg):
    server = bot.get_guild (715077503948947500)
    await ctx.send(f"{server.roles[int(arg)]}")

@bot.command()
async def locations(ctx, arg):
    server = bot.get_guild (715077503948947500)
    member = server.get_member(ctx.author.id)
    if arg == 'info':
        await ctx.send("The following locations are available:\n 1. Kinloch Park Middle\n 2. Nautilus Middle\n 3. NMB Library")
    if arg == "1":
        for kp in member.roles[1:]:
            if kp.name == "Nautilus" or "NMB Library":
                await member.remove_roles(member.roles[1], reason='user attempted to enroll in multiple locations')
                await ctx.send(f"You can't be enrolled in multiple locations")
        await member.add_roles(server.roles[1], reason='user indicated they attend Kinloch Park', atomic = True)
        await ctx.send(f"You are now enrolled at {server.roles[1]} {ctx.author.mention}")
            
    if arg == "2":
        for naut in member.roles[1:]:
            if naut.name == "Kinloch Park" or "NMB Library":
                await member.remove_roles(member.roles[1], reason='user attempted to enroll in multiple locations')
                await ctx.send(f"You can't be enrolled in multiple locations")
        await member.add_roles(server.roles[2], reason='user indicated they attend Kinloch Park', atomic = True)
        await ctx.send(f"You are now enrolled at {server.roles[2]} {ctx.author.mention}")

    if arg == "3":
        for nmb in member.roles[1:]:
            if nmb.name == "Kinloch Park" or "Nautilus":
                await ctx.send(f"You can't be enrolled in multiple locations")
                await member.remove_roles(member.roles[1], reason='user attempted to enroll in multiple locations')
        await member.add_roles(server.roles[3], reason='user indicated they attend Kinloch Park', atomic = True)
        await ctx.send(f"You are now enrolled at {server.roles[3]} {ctx.author.mention}")

    if arg == 'purge':
        for n in member.roles[1:]:
            if n.name == "Kinloch Park" or n.name == "Nautilus"or n.name =="NMB Library":
                await member.remove_roles(member.roles[1], reason ='user requested a purge of location tags')
        await ctx.send(f"Purge completed")

@bot.event
async def on_connect():
    print ('I have successfully logged in as {0.user}'.format(bot))


@bot.event 
async def on_disconnect():
    print ("I have lost connection, please troubleshoot")


@bot.event
async def on_ready():
    server = bot.get_guild (715077503948947500)
    print ('I have fully initialized as {0.user}'.format(bot))
    print ('joined '+ str(server))

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello there {ctx.author.name}")

@bot.command()
async def students(ctx):
    server = bot.get_guild (715077503948947500)
    x = server.roles[4].members
    students = []
    for count in x:
        students.append(count.name)
    await ctx.send(f" AI Academy currently has:```{len(students)} students```")

@bot.command()
async def dm(ctx):
    await ctx.author.send (""""Hello I am the official AI Academy bot, Reginald!
You might notice that the AI Academy discord is empty, but that's not the case. 
First, let me ask you, what locationg are you from?
1. Nautilus Middle 
2. Kinloch Park Middle
3. NMB Library""")

@bot.command()
async def roles(ctx): 
    server = bot.get_guild (715077503948947500)
    member = server.get_member(ctx.author.id)
    member_roles = member.roles[1:]
    role_names = []
    for name in member_roles:
        role_names.append(name.name)
    await ctx.send(f'your roles are:\n```{role_names}```')

@bot.command()
async def guildroles(ctx):
    server = bot.get_guild (715077503948947500)
    member = server.get_member(ctx.author.id)
    server_role_names = []
    for name in server.roles[1:]:
        server_role_names.append(name.name)
    await ctx.send(f'{server_role_names}')

#Location commands and responses_________________________________________________________________________________________________________________________________________________   

          

#end of Location commands and replies_____________________________________________________________________________________________________________________________________________

@bot.event
async def on_member_join(member):
    await member.send("Hello I am the official AI Academy bot, Reginald!\n"
    "You might notice that the AI Academy discord is empty, but that's not the case.\n" 
    "First, let me ask you, what locationg are you from?\n"
    "1. Nautilus Middle\n" 
    "2. Kinloch Park Middle\n"
    "3. NMB Library\n")

bot.run(token.read())